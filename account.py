import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

class Account:
    def __init__(self):
        __SPOTIPY_CLIENT_ID     = os.getenv('SPOTIPY_CLIENT_ID')
        __SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
        __SPOTIPY_REDIRECT_URI  = os.getenv('SPOTIPY_REDIRECT_URI')
        __SCOPE                 = 'playlist-modify-public playlist-modify-private playlist-read-private ugc-image-upload'

        self.__sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id     = __SPOTIPY_CLIENT_ID,
            client_secret = __SPOTIPY_CLIENT_SECRET,
            redirect_uri  = __SPOTIPY_REDIRECT_URI,
            scope         = __SCOPE
        ))
        
    def get_user(self):
        return self.__sp
    
    def get_user_id(self):
        return self.__sp.current_user()['id']
    