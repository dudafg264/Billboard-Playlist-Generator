import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import os

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
username = os.getenv('username')
redirect_uri = os.getenv('redirect_uri')

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

sp = spotipy.Spotify(
    auth_manager= SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=redirect_uri,
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username=username,
    )
)
user_id = sp.current_user()["id"]
create_playlist = sp.user_playlist_create(user=username, name=f"{date} Playlist", public=False)

response = requests.get(url=URL, headers=header)
response_text = response.text

all_songs = []
if response.status_code == 200:
    soup = BeautifulSoup(response_text, "html.parser")
    song_names_spans = soup.select("li ul li h3")
    for song in song_names_spans:
        song_names = song.getText().strip()
        try:
            results = sp.search(q=song_names, type='track', limit=1)
            track_uri = results['tracks']['items'][0]['uri']
            all_songs.append(track_uri)
        except Exception as e:
            print(f"Erro ao buscar a música '{song_name}' no Spotify: {e}")

    if all_songs:
        try:
            add_tracks = sp.user_playlist_add_tracks(user=username, playlist_id=create_playlist['uri'], tracks=all_songs)

        except Exception as e:
            print(f"Erro ao adicionar faixas à playlist: {e}")
    else:
        print("Nenhuma faixa encontrada para adicionar à playlist.")

