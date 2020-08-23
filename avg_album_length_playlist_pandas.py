import spotipy
import pandas as pd
import boto3
from io import StringIO
from datetime import datetime
import matplotlib.pyplot as plt

from config.playlists import spotify_playlists
from tools.playlists import get_artists_from_playlist

spotify = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())


artists = get_artists_from_playlist(spotify_playlists()['rap_caviar'])

final_data_dictionary = {'Year Released': [],
                         'Album Length': [],
                         'Album Name': [],
                         'Artist': []}


def format_df(unformatted_dataframe: pd.DataFrame) -> pd.DataFrame:
    df = unformatted_dataframe.set_index('Year Released')
    df = df.drop_duplicates(subset='Album Name')
    df = df.mean(level=0) # Average of album length by index
    df = df.sort_index()
    df['Album Length'] = df['Album Length']*0.0000002777778
    chart = df.plot(use_index=True, y='Album Length', kind='bar', legend=False)
    chart.set_ylabel("Average Album Length (hours)")
    chart.set_xlabel("Year Released")
    return df


def gather_data():
    # TODO make a generic function that both this and avg_album_length_artists.py can use
    # For every artist we're looking for
    for artist in artists.keys():
        artists_albums = spotify.artist_albums(artist, album_type='album', limit=50)
        # For all of their albums
        for album in artists_albums['items']:
            if 'GB' in artists_albums['items'][0]['available_markets']:
                album_data = spotify.album(album['uri'])
                # For every song in the album
                album_length_ms = 0
                for song in album_data['tracks']['items']:
                    # TODO consider album popularity
                    album_length_ms = song['duration_ms'] + album_length_ms
                final_data_dictionary['Album Length'].append(album_length_ms)
                final_data_dictionary['Year Released'].append(album_data['release_date'][:4])
                final_data_dictionary['Album Name'].append(album_data['name'])
                final_data_dictionary['Artist'].append(album_data['artists'][0]['name'])
    return final_data_dictionary


if __name__ == '__main__':
    data = gather_data()
    print(data['Album Length'])
    print(data['Year Released'])
    print(data['Album Name'])

    df = pd.DataFrame(data)
    formatted_df = format_df(unformatted_dataframe=df)
    # plt.show()

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_resource = boto3.resource('s3')
    date = datetime.now()
    filename = f'{date.year}/{date.month}/{date.day}/rapcaviar_albums.csv'
    s3_resource.Object('spotify-analysis-data', filename).put(Body=csv_buffer.getvalue())


