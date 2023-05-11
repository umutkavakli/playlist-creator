import base64
import requests
import uuid
from PIL import Image


class Playlist:
    def __init__(self, user_object, user_id):
        self.__user = user_object
        self.__user_id = user_id

    def create(self, name, description, public=False):
        if name == "":
            name = "bot playlist"

        self.__new_playlist = self.__user.user_playlist_create(
            user        = self.__user_id,
            name        = name,
            public      = public,
            description = description
        )

    def add_tracks(self, tracks):
        self.__user.user_playlist_add_tracks(
            user        = self.__user_id,
            playlist_id = self.__new_playlist['id'],
            tracks      = tracks
        )

    def get_playlist_id(self):
        return self.__new_playlist['id']


class Track:
    def __init__(self, user_object):
        self.__user_object = user_object

    def get_tracks(self, track_list):
        track_list_ids = []
        tracks = []
        for (track_name, artist_name) in track_list:
            results = self.__user_object.search(q=f'track:{track_name} artist:{artist_name}', type='track', limit=1)['tracks']['items']

            if (results):
                track_list_ids.append(results[0]['id'])
                tracks.append((track_name, artist_name))

        return track_list_ids, tracks

class Cover:
    def __init__(self, user_object):
        self.__user = user_object
        self.__id = None

    def download_img(self, url):
        response = requests.get(url)
        self.__id = uuid.uuid4()
        
        with open(f'images/image{self.__id}.jpg', 'wb') as file:
            file.write(response.content)
        image = Image.open(f'images/image{self.__id}.jpg')
        image.save(f'images/image{self.__id}.jpg', optimize=True, quality=95)

    def b64_encode(self):
        with open(f'images/image{self.__id}.jpg', 'rb') as image:
            return base64.b64encode(image.read())

    def upload(self, playlist_id, b64):
        self.__user.playlist_upload_cover_image(playlist_id, b64)