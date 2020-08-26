import matplotlib.pyplot as plt
import csv
import pandas as pd

grateful_album_data = '/Users/liamhartley/IdeaProjects/spotify_analysis/data/djkhaled_grateful.csv'
reader = csv.DictReader(open(grateful_album_data))
grateful_data = {}
for row in reader:
    for column, value in row.items():
        grateful_data.setdefault(column, []).append(value)

grateful_data['popularity'] = [int(x) for x in grateful_data['popularity']]

df = pd.DataFrame(grateful_data)

df = df.set_index('song_name')
chart = df.plot.bar(width=0.8)
chart.set_ylabel("Tracks Spotify Popularity Score")
chart.get_legend().remove()
plt.show()

