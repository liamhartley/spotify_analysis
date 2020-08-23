import spotipy

spotify = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())


def get_artists_from_playlist(playlist_uri):
    '''
    :param playlist_uri: Playlist to analyse
    :return: A dictionary(artist uri : artist name) of all primary artists in a playlist.
    '''
    artists = {}
    playlist_tracks = spotify.playlist_tracks(playlist_id=playlist_uri)
    for song in playlist_tracks['items']:
        if song['track']:
            print(song['track']['artists'][0]['name'])
            artists[song['track']['artists'][0]['uri']] = song['track']['artists'][0]['name']
    return artists
