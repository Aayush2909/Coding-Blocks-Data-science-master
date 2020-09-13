import numpy as np
import pandas as pd
import warnings
from matplotlib import pyplot as plt
import seaborn as sns

def predict(movie_name, ratings, movies):
    
    ratings = ratings.iloc[:,0:3]
    movies = movies[['MovieID', 'Title']]
    df = pd.merge(ratings, movies, on='MovieID')
    
    titles = df.groupby('Title').mean()[['Rating']]
    titles['Num of ratings'] = df.groupby('Title').count()['Rating']
    
    
    #Data Visulaisation
    plt.figure(figsize=(10,10))
    
    plt.subplot(1,2,1)
    plt.hist(titles['Num of ratings'], bins = 20)
    
    plt.subplot(1,2,2)
    plt.hist(titles['Rating'], bins=30)
    
    sns.jointplot(x='Rating', y='Num of ratings', data=titles, alpha=0.5)
    plt.show()
    
    movie_mat = df.pivot_table(index='UserID', columns='Title', values='Rating')
    movie_rating = movie_mat[movie_name]
    
    similar_movie = movie_mat.corrwith(movie_rating)
    corr_df = pd.DataFrame(similar_movie, columns=['Correlation'])
    corr_df.dropna(inplace=True)
    corr_df = corr_df.join(titles['Num of ratings'])
    corr_df = corr_df[corr_df['Num of ratings'] > 100]
    
    res = corr_df.sort_values(by='Correlation', ascending=False).iloc[1:,:]
    
    return res
    

if __name__ == '__main__':
    
    warnings.filterwarnings('ignore')
    ratings = pd.read_csv("C:\\Users\\AaYush\\Downloads\\Compressed\\ml-1m\\ratings.dat", sep = '::', names=['UserID', 'MovieID', 'Rating', 'Timestamp'])
    movies = pd.read_csv("C:\\Users\\AaYush\\Downloads\\Compressed\\ml-1m\\movies.dat", sep='::', names=['MovieID', 'Title', 'Genres'])
    
    
    movie_name = input('Movie that you watched recenty: ')
    
    res = predict(movie_name, ratings, movies)
    
    print('\nTop 10 recommended movies- \n')
    for i,m in enumerate(res.index):
        if i < 10:
            print('\t{}'.format(m))
