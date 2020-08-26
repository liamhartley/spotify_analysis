import matplotlib.pyplot as plt
import csv

drake_file_location = '/Users/liamhartley/IdeaProjects/spotify_analysis/data/drake_discography.csv'
reader = csv.DictReader(open(drake_file_location))
drake = {}
for row in reader:
    for column, value in row.items():
        drake.setdefault(column, []).append(value)

ye_file_location = '/Users/liamhartley/IdeaProjects/spotify_analysis/data/kanye_discography.csv'
reader = csv.DictReader(open(ye_file_location))
ye = {}
for row in reader:
    for column, value in row.items():
        ye.setdefault(column, []).append(value)

ye['Year Released'] = [int(x)+0.15 for x in ye['Year Released']]
ye['Album Length'] = [int(x)*0.0000002777778 for x in ye['Album Length']]
drake['Year Released'] = [int(x)-0.15 for x in drake['Year Released']]
drake['Album Length'] = [int(x)*0.0000002777778 for x in drake['Album Length']]

ax = plt.subplot(111)
ax.bar(ye['Year Released'], ye['Album Length'], width=0.3, color='b', align='center', label='Kanye')
ax.bar(drake['Year Released'], drake['Album Length'], width=0.3, color='r', align='center', label='Drake')

ax.set_ylabel("Album Length (hours)")
ax.set_xlabel("Year Released")

ax.legend(loc='upper left')

ax.ticklabel_format(useOffset=False, style='plain')

plt.show()

