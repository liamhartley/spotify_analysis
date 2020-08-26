import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/liamhartley/IdeaProjects/spotify_analysis/data/rapcaviar_deluxe.csv', encoding='iso-8859-1')

df = df.set_index('Year Released')
df = df.drop_duplicates(subset='Album Name')
df = df.mean(level=0)
df = df.sort_index()
df['Album Length'] = df['Album Length']*0.0000002777778
# chart = df.plot.bar(rot=2)
chart = df.plot(use_index=True, y='Album Length', kind='bar', legend=False)
chart.set_ylabel("Average Album Length (hours)")
chart.set_xlabel("Year Released")
plt.show()
