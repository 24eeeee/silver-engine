import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.options.display.expand_frame_repr = False

data = pd.read_csv("data/anime.csv")

print(data.head(10)) # 2

data['Episodes'] = data['Episodes'].replace('?', np.nan)
data['Voters'] = data['Voters'].str.replace(",", "")
data = data.astype({'Episodes': 'float32',
                    'Title': 'string',
                    'Production': 'string',
                    'Source': 'string',
                    'Genre': 'string',
                    'Airdate': 'string',
                    'Voters': 'int32',
                    'Rating': 'float32',
                    'Theme': 'string'})
print(data.info()) # 3

data.rename(columns=dict(zip(data.columns, list(map(lambda x: x.lower().replace(' ', '_'), data.columns)))), inplace=True) # 4
print(data.describe([.25, .5, .75, .9])) # 5

print(data.production.value_counts())
print(data.source.value_counts())
print(data.genre.value_counts()) # 6

# 7
# Pandas умеет работать с NaN ячейками с полным пониманием того, что это отсутствующие данные,
# а не, например, 0. Поэтому оставляем NaN-ы в таблице на усмотрение библиотечных функций.

data.production.value_counts().sort_values().plot.bar()
print(data['production'].value_counts().keys()[0])
plt.show() # 8a

data['episodes'].value_counts().plot.bar()
print(data['episodes'].value_counts().values[0])
plt.show() # 8b

data['source'].value_counts().head(3).plot.bar()
print(data['source'].value_counts().keys()[0])
plt.show() # 8c

data['theme'].value_counts().plot.bar()
print(data['theme'].value_counts().keys()[0])
plt.show() # 8d


a = pd.Series(filter("????".__ne__, map(lambda x: x.split(',')[1].strip(), data.airdate.dropna()))).value_counts()
a.plot.bar()
print(a.keys()[0])
plt.show() # 8e


productions = data[['production', 'rating']].dropna().groupby('production').mean().sort_values('rating')
productions.plot.bar()
print(productions.tail(3).sort_values('rating', ascending=False))
plt.show() # 9

data['rating'].plot.hist(bins=range(11))
plt.show() # 10

genres = data.replace('-', np.nan).copy()
genres = genres.assign(genre=genres['genre'].str.split(',')).explode('genre')
genres = genres[['genre', 'rating']].groupby('genre').mean().sort_values('rating')
genres.plot.bar()
plt.show()

themes = data.replace('-', np.nan).copy()
themes = themes.assign(theme=themes['theme'].str.split(',')).explode('theme')
themes = themes[['theme', 'rating']].groupby('theme').mean().sort_values('rating')
themes.plot.bar()
plt.show() # 11

data.plot(x='voters', y='rating')
plt.show()
print(data.voters.sort_values()) # 12
