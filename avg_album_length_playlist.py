import spotipy
import csv
import boto3
from datetime import datetime

from config.playlists import spotify_playlists
from tools.playlists import get_artists_from_playlist
from rapcaviar_transformer import get_artists

spotipy_object = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())


artists = get_artists_from_playlist(spotify_playlists()['rap_caviar'])

final_data_dictionary = {'Year Released': [],
                         'Album Length': [],
                         'Album Name': [],
                         'Artist': []}


def gather_data_local():
    # For every artist we're looking for
    with open("rapcaviar_albums.csv", 'w') as file:
        header = ['Year Released', 'Album Length', 'Album Name', 'Artist']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        albums_obtained = []

        artists = get_artists()

        # for artist in artists.keys():
        for artist in artists:
            print(artist)
            artists_albums = spotipy_object.artist_albums(artist, album_type='album', limit=50)
            # For all of their albums
            for album in artists_albums['items']:
                if 'GB' and 'US' in album['available_markets']:
                    key = album['name'] + album['artists'][0]['name'] + album['release_date'][:4]
                    if key not in albums_obtained:
                        albums_obtained.append(key)
                        album_data = spotipy_object.album(album['uri'])
                        # For every song in the album
                        album_length_ms = 0
                        for song in album_data['tracks']['items']:
                            album_length_ms = song['duration_ms'] + album_length_ms
                        writer.writerow({'Year Released': album_data['release_date'][:4],
                                         'Album Length': album_length_ms,
                                         'Album Name': album_data['name'],
                                         'Artist': album_data['artists'][0]['name']})
    return final_data_dictionary


def gather_data():
    # For every artist we're looking for
    with open("/tmp/rapcaviar_albums.csv", 'w') as file:
        header = ['Year Released', 'Album Length', 'Album Name', 'Artist']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for artist in artists.keys():
            artists_albums = spotipy_object.artist_albums(artist, album_type='album', limit=50)
            # For all of their albums
            for album in artists_albums['items']:
                if 'GB' in artists_albums['items'][0]['available_markets']:
                    album_data = spotipy_object.album(album['uri'])
                    # For every song in the album
                    album_length_ms = 0
                    for song in album_data['tracks']['items']:
                        # TODO consider album popularity
                        album_length_ms = song['duration_ms'] + album_length_ms
                    writer.writerow({'Year Released': album_data['release_date'][:4],
                                     'Album Length': album_length_ms,
                                     'Album Name': album_data['name'],
                                     'Artist': album_data['artists'][0]['name']})

    s3_resource = boto3.resource('s3')
    date = datetime.now()
    filename = f'{date.year}/{date.month}/{date.day}/rapcaviar_albums.csv'
    s3_resource.Object('spotify-analysis-data', filename).upload_file("/tmp/rapcaviar_albums.csv")

    return final_data_dictionary


def lambda_handler(event, context):
    gather_data()


if __name__ == '__main__':
    data = gather_data_local()

    s3_resource = boto3.resource('s3')
    date = datetime.now()
    filename = f'{date.year}/{date.month}/{date.day}/rapcaviar_albums.csv'
    s3_resource.Object('spotify-analysis-data', filename).upload_file("rapcaviar_albums.csv")




