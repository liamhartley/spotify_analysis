import spotipy
import csv

from config.artists import spotify_artists

spotify = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

final_data_dictionary = {'Year Released': [],
                         'Album Length': [],
                         'Artist': [],
                         'Album Name': []}

artist = spotify_artists()
artists_albums = spotify.artist_albums(artist['Drake'], album_type='album', limit=50)

with open("data/drake_discography.csv", 'w') as file:
    header = final_data_dictionary.keys()
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    # For all of the artists albums
    for album in artists_albums['items']:
        if 'GB' in artists_albums['items'][0]['available_markets']:
            album_data = spotify.album(album['uri'])
            # For every song in the album
            album_length_ms = 0
            for song in album_data['tracks']['items']:
                album_length_ms = song['duration_ms'] + album_length_ms
            writer.writerow({'Year Released': album_data['release_date'][:4],
                             'Album Length': album_length_ms,
                             'Album Name': album_data['name'],
                             'Artist': album_data['artists'][0]['name']})
