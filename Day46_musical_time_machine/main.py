from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")

scope = "playlist-modify-private"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

music_url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=music_url)

soup = BeautifulSoup(response.text, "html.parser")
song_title = soup.select(selector="span.chart-element__information__song.text--truncate.color--primary")

song_name_list = [item.string for item in song_title]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope,
    show_dialog=True,
    cache_path="token.txt"
))

uri_list = []
for song_name in song_name_list:
    result = sp.search(q=f"track:{song_name} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        pass
    else:
        uri_list.append(uri)

user_id = sp.current_user()["id"]

new_playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
new_playlist_id = new_playlist["id"]
sp.playlist_add_items(playlist_id=new_playlist_id, items=uri_list)

# print(uri_list)
print(sp.playlist(new_playlist_id))