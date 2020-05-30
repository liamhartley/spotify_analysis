import spotipy
import pandas as pd
import matplotlib.pyplot as plt

from config.artists import spotify_artists

spotify = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

final_data_dictionary = {'Year Released': [],
                         'Album Length': [],
                         'Artist Name': [],
                         'Album Name': []}

# For every artist we're looking for
for artist in spotify_artists().keys():
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
            final_data_dictionary['Artist Name'].append(album_data['artists'][0]['name'])
            final_data_dictionary['Album Name'].append(album_data['name'])

print(final_data_dictionary['Album Length'])
print(final_data_dictionary['Year Released'])
print(final_data_dictionary['Artist Name'])
print(final_data_dictionary['Album Name'])

df = pd.DataFrame(data=final_data_dictionary)
df = df.set_index('Year Released')
df = df.drop_duplicates(subset='Album Name')
df = df.mean(level=0)
df = df.sort_index()
df['Album Length'] = df['Album Length']*0.0000002777778
chart = df.plot.bar(rot=2)
# chart = df.plot(use_index=True, y='Album Length', kind='bar', legend=False)
chart.set_ylabel("Average Album Length (hours)")
chart.set_xlabel("Year Released")
plt.show()

