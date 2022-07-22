# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:20:52 2022

@author: Duda Bastos
"""

import pandas as pd

pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

pd.Series([1, 2, 3, 4, 5])

pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

wine_reviews = pd.read_csv("C:/uni/Intro Ciencia Dados/winemag-data-130k-v2.csv", index_col=0)

pd.set_option('max_rows', 5)

wine_reviews.shape

wine_reviews.head()

wine_reviews.country
wine_reviews['country'][1]
wine_reviews.iloc[0]
wine_reviews.iloc[:, 0]
wine_reviews.iloc[:3, 0]
wine_reviews.iloc[1:3, 0]
wine_reviews.iloc[[0, 1, 2], 0]
wine_reviews.iloc[-5:]
wine_reviews.loc[1, 'country']
wine_reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
wine_reviews.set_index("title")
wine_reviews.country == 'Italy'
wine_reviews.loc[wine_reviews.country == 'Italy']
wine_reviews.loc[(wine_reviews.country == 'Italy') & (wine_reviews.points >= 90)]
wine_reviews.loc[(wine_reviews.country == 'Italy') | (wine_reviews.points >= 90)]
wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France'])]
wine_reviews.loc[wine_reviews.price.notnull()]
wine_reviews['critic'] = 'everyone'
wine_reviews['critic']
wine_reviews['index_backwards'] = range(len(wine_reviews), 0, -1)
wine_reviews['index_backwards']

wine_reviews.points.describe()
wine_reviews.taster_name.describe()
wine_reviews.points.mean()
wine_reviews.points.median()
wine_reviews.taster_name.unique()
wine_reviews.taster_name.value_counts()
centered_price = wine_reviews.price - wine_reviews.price.mean()
centered_price

wine_review_points_mean = wine_reviews.points.mean()
wine_reviews.points.map(lambda p: p - wine_review_points_mean)
def remean_points(row):
    row.points = row.points - wine_review_points_mean
    return row
wine_reviews.apply(remean_points, axis='columns')
bargain_idx = (wine_reviews.points / wine_reviews.price).idxmax() #Melhor vinho mais barato
wine_reviews.loc[bargain_idx, 'title']

n_trop = wine_reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = wine_reviews.description.map(lambda desc: "fruity" in desc).sum()
pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = wine_reviews.apply(stars, axis='columns')


reviews=wine_reviews
wine_reviews.groupby('points').points.count()
wine_reviews.groupby('points').price.min()
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
reviews.groupby(['country']).price.agg([len, min, max])
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed
mi = countries_reviewed.index
type(mi)
countries_reviewed.reset_index()
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')
countries_reviewed.sort_values(by='len', ascending=False)
countries_reviewed.sort_index()
countries_reviewed.sort_values(by=['country', 'len'])

reviews.price.dtype
reviews.dtypes
reviews.points.astype('float64')
reviews.index.dtype
reviews[pd.isnull(reviews.country)]
reviews.region_2.fillna("Unknown")
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

reviews.rename(columns={'points': 'score'})
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

canadian_youtube = pd.read_csv("C:/uni/Intro Ciencia Dados/CAvideos.csv")
british_youtube = pd.read_csv("C:/uni/Intro Ciencia Dados/GBvideos.csv")
pd.concat([canadian_youtube, british_youtube])
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
left.join(right, lsuffix='_CAN', rsuffix='_UK')


wine_reviews.head(2)
wine_review_points_mean = wine_reviews.points.mean()
wine_reviews.points - wine_review_points_mean
wine_reviews.country + " - " + wine_reviews.region_1




pd.DataFrame({'Apples': [30], 'Bananas': [21]}, index=[0])

pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name= 'Dinner')

ingredients.to_csv("C:/uni/Intro Ciencia Dados/ingredientes.csv")