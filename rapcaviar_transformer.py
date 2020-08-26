
import spotipy

spotipy_object = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())


def get_artists(filepath='/Users/liamhartley/IdeaProjects/spotify_analysis/data/rapcaviar_artists.csv'):
    with open(filepath, 'r') as file:
        artists = []
        for row in file:
            artists.append(spotipy_object.search(row)['tracks']['items'][0]['artists'][0]['uri'])
    return artists


