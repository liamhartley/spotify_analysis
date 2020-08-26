import spotipy
import csv

spotipy_object = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())


def gather_data_local():
    filepath = '/Users/liamhartley/IdeaProjects/spotify_analysis/data/djkhaled_grateful.csv'
    with open(filepath, 'w') as file:
        header = ['song_name', 'popularity']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        album = spotipy_object.album(album_id='spotify:album:4JBZ0QHveEpESepanNBG8A')
        for song in album['tracks']['items']:
            track = spotipy_object.track(track_id=song['uri'])
            writer.writerow({'song_name': track['name'],
                             'popularity': track['popularity']})

    return


if __name__ == '__main__':
    gather_data_local()
