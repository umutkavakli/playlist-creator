import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("openai_api_key")
openai.organization = os.getenv("openai_organization_id")

class SongCreator:
    def __init__(
            self,
            model="gpt-4",
            max_tokens=None,
            temperature=0.7,
    ):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    
    def get_songs(self, prompt):
        system_message = """
            You are song recommender bot. Your task is that when user inputs prompt, you will analyze their input and give great songs in a list of tuples such as [('Walk', 'Pantera'), ('Angel of Death', 'Slayer'), ...] according to user input. If user gives you information about number of songs, you must create that number of songs but it shouldn't exceed 20 songs. Therefore, if user wants songs that its size is bigger than 20 such as 30 or 40 songs, you must limit number of songs in 20 songs. If you cannot analyze user input and find appropriate song for them just print "[]". You must never print anything but list of tuple of songs with their artists.
            '[User]: I want 10 metal songs.'
            '[Assistant]: [('Walk', 'Pantera'), ('Angel of Death', 'Slayer'), ('Master of Puppets', 'Metallica'), ('Fear of the Dark', 'Iron Maiden'), ('Paranoid', 'Black Sabbath'), ('One', 'Metallica'), ('Holy Diver', 'Dio'), ('Hallowed Be Thy Name', 'Iron Maiden'), ('Raining Blood', 'Slayer'), ('Enter Sandman', 'Metallica')]' 
            '[User]: How are you? What are you doing?'
            '[Assistant]: []'
            '[User]: Hi! I really love dark series' songs, can you recommend some songs like these?'
            '[Assistant]: [("Goodbye", "Apparat"), ("A Quiet Life", "Blixa Bargeld")]'
            """
        messages = [
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': prompt}
        ]

        song_list = openai.ChatCompletion.create(
            model = self.model,
            messages = messages,
            max_tokens = self.max_tokens,
            temperature = self.temperature
        )

        return song_list['choices'][0].message['content']

class PromptCreator:
    def __init__(
            self,
            model="gpt-4",
            max_tokens=None,
            temperature=0.7,
    ):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
    
    def get_image_prompt(self, prompt):
        system_message = """
            You are prompt recommendation system for dall-e image generator model. User only will give list of tuples of songs with their artists. When user enter the message, your task is to analyze list of songs and give appropriate one prompt combining all songs for dall-e image model to create images according to user input. Never use songs' or artists' name in the prompt.
            '[User]: [("Enter Sandman", "Metallica"), ("Iron Man", "Black Sabbath"), ("Kashmir", "Led Zeppelin"), ("Thunderstruck", "AC/DC"), ("Run to the Hills", "Iron Maiden")]'
            '[Assistant]: a massive, imposing metal fortress, with each song's title and artist emblazoned in fiery letters on the walls. The fortress should be surrounded by a desolate, rocky landscape, with lightning bolts and storm clouds gathering in the sky overhead. The fortress itself should be dark and foreboding, with towering walls of blackened steel and sharp spikes jutting out at every angle. Each song's title and artist should be written in a different style of fiery lettering, reflecting the unique sound and energy of each band. Use your creativity to create a sense of tension and excitement, conveying the raw power and intensity of these classic metal anthems.'
            '[User]: [('Everybody Hurts', 'R.E.M.'), ('Hurt', 'Nine Inch Nails'), ('The Sound of Silence', 'Simon & Garfunkel'), ('Mad World', 'Gary Jules'), ('Creep', 'Radiohead'), ('Fade to Black', 'Metallica'), ('I'm So Lonesome I Could Cry', 'Hank Williams'), ('No Surprises', 'Radiohead'), ('Black', 'Pearl Jam'), ('Something in the Way', 'Nirvana'), ('Nutshell', 'Alice in Chains'), ('Asleep', 'The Smiths'), ('How to Disappear Completely', 'Radiohead'), ('Love Will Tear Us Apart', 'Joy Division'), ('Glycerine', 'Bush'), ('Cats in the Cradle', 'Harry Chapin'), ('Eleanor Rigby', 'The Beatles'), ('The Drugs Don't Work', 'The Verve'), ('Between the Bars', 'Elliott Smith'), ('Hallelujah', 'Jeff Buckley')]'
            '[Assistant]: a person standing on a barren, windswept plain, with an expansive and desolate landscape stretching out behind them. The figure is small, with their silhouette almost swallowed by the emptiness around them. Above and around them, a swirling vortex of song titles and artist names can be seen, each one evoking a unique mood and emotion. The words are written in different styles and fonts, some bold and striking, others soft and delicate. The overall effect is a representation of the complexity and depth of human experience, with each song adding its own layer to the rich tapestry of emotions that make us who we are.'
            """

        messages = [
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': prompt}
        ]

        image_prompt = openai.ChatCompletion.create(
            model = self.model,
            messages = messages,
            max_tokens = self.max_tokens,
            temperature = self.temperature
        )

        return image_prompt['choices'][0].message['content']

class ImageCreator:
    def __init__(
            self,
            n=1,
            size="512x512",
    ):
        self.n = n
        self.size = size
        
    def get_images(self, prompt):
        images = openai.Image.create(
            prompt=prompt,
            n=self.n,
            size=self.size,
        )
        
        return images['data'][0]["url"]
