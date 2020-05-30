import spotipy
import pandas as pd
import matplotlib.pyplot as plt

from config.playlists import spotify_playlists
from tools.playlists import get_artists_from_playlist

spotify = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())


artists = get_artists_from_playlist(spotify_playlists()['rap_caviar'])

final_data_dictionary = {'Year Released': [],
                         'Album Length': [],
                         'Album Name': []}


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


def gather_data() -> dict[str:str]:
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
    return final_data_dictionary


if __name__ == '__main__':
    data = gather_data()
    print(data['Album Length'])
    print(data['Year Released'])
    print(data['Album Name'])

    df = pd.DataFrame(data)
    formatted_df = format_df(unformatted_dataframe=df)
    plt.show()
