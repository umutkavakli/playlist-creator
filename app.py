import ast
import gradio as gr
from account import Account
from playlist import Cover, Playlist, Track
from bot import SongCreator, ImageCreator, PromptCreator

user = Account()

playlist_object = Playlist(user.get_user(), user.get_user_id())
track_object = Track(user.get_user())
cover_object = Cover(user.get_user())

song_creator = SongCreator(max_tokens=1024)
prompt_creator = PromptCreator(max_tokens=1024)
image_creator = ImageCreator()

def create_playlist(playlist_name, public, description, song_list, url):
    # create playlist
    playlist_object.create(name=playlist_name, public=public, description=description)
    
    # get track ids then add tracks to playlist
    track_ids, tracks = track_object.get_tracks(song_list)
    playlist_object.add_tracks(track_ids)

    # get the image and update cover of playlist
    cover_object.download_img(url)
    b64 = cover_object.b64_encode()
    cover_object.upload(playlist_object.get_playlist_id(), b64)

    return tracks


def show_songs(song_list):
    output = ""
    for i, (song, artist) in enumerate(song_list):
        output += f"{i+1}) {song} - {artist}\n"

    return output

def prompt(prompt_text, playlist_name, public, description):
    song_list = song_creator.get_songs(prompt_text)
    image_prompt = prompt_creator.get_image_prompt(song_list)
    image = image_creator.get_images(image_prompt)

    tracks = create_playlist(playlist_name, public, description, ast.literal_eval(song_list.strip()), image)
    return image, show_songs(tracks)

with gr.Blocks(theme=gr.themes.Monochrome(), title="Song Creator", ) as demo:
    with gr.Row(variant="panel") as row:
        with gr.Column():
            # user interface inputs
            prompt_text = gr.TextArea(label="Prompt")
            playlist_name = gr.Textbox(label="Playlist Name")
            public = gr.Checkbox(label="Public")
            description = gr.Textbox(label="Description")
            
            btn = gr.Button("Create Playlist!")
        with gr.Column():
                image = gr.Image(shape=(512, 512), label="Cover Image")
                output_songs = gr.TextArea(label="Songs")

        btn.click(
            prompt, 
            [prompt_text, playlist_name, public, description],
            [image, output_songs]
        )

demo.launch()

