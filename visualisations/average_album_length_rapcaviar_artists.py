import csv
import numpy
import pandas as pd
import matplotlib.pyplot as plt

ax = plt.gca()


def format_maindf(filepath: str):
    df = pd.read_csv(filepath, encoding='iso-8859-1')

    df = df.set_index('ï»¿Year Released')
    df = df.mean(level=0)
    df = df.sort_index()
    df['Album Length'] = df['Album Length'] * 0.0000002777778
    df['Year Released'] = df.index
    return df


def calculate_trendline_function(df: pd.DataFrame):
    z = numpy.polyfit(df['Year Released'], df['Album Length'], 1)
    p = numpy.poly1d(z)
    # Unable to plot above, writing p out
    print(f'Trendline equation: {p}\n\n')
    return p


def trendlines(filepath: str):
    trend_raw = filepath
    reader = csv.DictReader(open(trend_raw))
    trend_data = {}
    for row in reader:
        for column, value in row.items():
            trend_data.setdefault(column, []).append(value)

    df_trend = pd.DataFrame(data=trend_data)
    df_trend.set_index('﻿year_released', inplace=True)
    df_trend = df_trend.sort_index()
    df_trend['album_length'] = [float(x) for x in df_trend['album_length']]

    return df_trend


if __name__ == '__main__':

    main_data_locations = {"/Users/liam.hartley/PycharmProjects/spotify_analysis/data/rapcaviar_deluxe.csv": '#138003',
                           "/Users/liam.hartley/PycharmProjects/spotify_analysis/data/rapcaviar_raw.csv": '#a8160c',
                           "/Users/liam.hartley/PycharmProjects/spotify_analysis/data/rapcaviar_standard.csv": '#091c85'}
    trendline_data_locations = {"/Users/liam.hartley/PycharmProjects/spotify_analysis/data/trendline_standard.csv":'#8597ff',
                                "/Users/liam.hartley/PycharmProjects/spotify_analysis/data/trendline_raw.csv": '#fc928b',
                                "/Users/liam.hartley/PycharmProjects/spotify_analysis/data/trendline_deluxe.csv": '#adffa1'}

    for main_data in main_data_locations.keys():
        df = format_maindf(filepath=main_data)
        chart = df.plot(use_index=True, y='Album Length', kind='bar', legend=False, ax=ax, color=main_data_locations[main_data])
        print(main_data)
        calculate_trendline_function(df)

    linestyle = "--"
    for trend_data in trendline_data_locations.keys():
        df_trend = trendlines(filepath=trend_data)
        df_trend.plot(use_index=True, y='album_length', kind='line', style=linestyle, legend=False, ax=ax, color=trendline_data_locations[trend_data])

    for label in ax.xaxis.get_ticklabels()[::2]:
        label.set_visible(False)

    ax.legend(labels=('Deluxe Album Trend', 'All Artist Albums Trend', 'Without Deluxe Trend',
                      'Deluxe Albums Only', 'All Artist Albums', 'Without Deluxe Albums'),
              loc='lower right')

    chart.set_ylabel("Average Album Length (hours)")
    chart.set_xlabel("Year Released")
    plt.draw()
    plt.savefig('viz_standard.png', dpi=100)
    plt.show()
