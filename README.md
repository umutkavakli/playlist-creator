# playlist-creator

Wouldn't it be great if someone could find songs based on our emotions or musical taste and create a playlist for us? Well, I have developed a program that does just that!

![](example.gif)

### Installation and Setup

<b>Step 1:</b> Clone the repository: 
```
git clone https://github.com/umutkavakli/playlist-creator.git
```
<b>Step 2:</b> Install dependencies:
```
cd playlist-creator/
mkdir images
python3 -m venv song_env
source song_env/bin/activate
pip install -r requirements.txt
```
<hr>

<b>Step 3:</b> Get credentials

Now, open <b>".env"</b> file. You must fill environment variables with your api keys: 

```
SPOTIPY_CLIENT_ID      = "YOUR-SPOTIFY-CLIENT-ID"
SPOTIPY_CLIENT_SECRET  = "YOUR-SPOTIFY-CLIENT-SECRET"
SPOTIPY_REDIRECT_URI   = "https://localhost:8080"

openai_api_key         = "YOUR-OPENAI-API-KEY"
openai_organization_id = "YOUR-OPENAI-ORGANIZATION-ID"
```

- Go to [Spotify Dashboard](https://developer.spotify.com/dashboard) page (login if you don't).
    - Create an app
    - You can copy <b>client id & client server</b> keys for spotify


* Go to [OpenAI API Keys](https://platform.openai.com/account/api-keys) page (register & login if you don't)
    * Create an API key
    * Copy & paste it to <b>openai_api_key</b> variable
* Go to [Organization Settings](https://platform.openai.com/account/org-settings) page
    * Copy & paste your organization id to <b>openai_organization_id</b> variable

## Usage

```
python3 app.py
```
<b>Note:</b> When you run the code for the first time, your browser will open new tab and you will see this on terminal:

```
Enter the URL you were redirected to: Opening in existing browser session.
```

You should copy the link in address bar of browser and paste it to the terminal, then press enter. This process is needed for getting token from spotify. You will be this only once because a .cache file will be created for next usages. 