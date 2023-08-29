import spotipy
import importlib
import os
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

creating_auth = importlib.import_module("creating-auth")
creating_auth.get_user("Harris")
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
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

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