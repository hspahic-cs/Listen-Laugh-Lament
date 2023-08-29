import spotipy
import importlib
import os
import requests
import lyricsgenius as lg

from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# Defining Constants
print(os.environ)
GENIUS = lg.Genius(os.getenv("GENIUS_ACCESS"), remove_section_headers=True)

def get_lyrics(song, artist):
    song = GENIUS.search_song(song, artist)
    return song.lyrics

def main():
    token = os.getenv("GENIUS_ACCESS")
    song_title = "Shape of You"  # replace with your desired song
    artist_name = "Ed Sheeran"  # replace with the artist's name

    
    print(get_lyrics(song_title, artist_name))


main()

'''
# Creating connection for spotify API
creating_auth = importlib.import_module("creating-auth")
creating_auth.get_user("Saoirse")

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Creating connection to Genius API




# auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)

# playlists = sp.current_user_recently_played()
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
# playlist = spotify.playlist(playlist_id, fields=None, market=None, additional_types=('track', ))

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])

os.environ.pop("SPOTIPY_CLIENT_ID")
os.environ.pop("SPOTIPY_CLIENT_SECRET")
'''