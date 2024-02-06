# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:36:20 2024

@author: bmaba
"""
import pandas

file=pandas.read_csv("movie_dataset.csv")

df=pandas.read_csv("movie_dataset.csv")


x = df["Revenue (Millions)"].mean()


df["Revenue (Millions)"].fillna(x, inplace = True) 


x = df["Metascore"].mean()

df["Metascore"].fillna(x, inplace = True) 

max_rating = df['Rating'].max()

print("\nRating:", max_rating)


# average of all the movies

print(df.describe())
      

#average revenue of movies from 2015 to 2017

filtered_data = df[(df["Year"]>=2015) & (df["Year"]<2017)]

Average_Revenue=filtered_data["Revenue (Millions)"].mean()

print(Average_Revenue)

#total movies in 2016
Movies_2016= df[(df["Year"]==2016)]

Movies_tot=len(Movies_2016)

print(Movies_tot)


#How many movies were directed by Christopher Nolan?

Christopher_Nolan_Movies= df[(df["Director"]=="Christopher Nolan")]

movies_tot=len(Christopher_Nolan_Movies)

print(movies_tot)

#How many movies in the dataset have a rating of at least 8.0

filtered_data = df[(df["Rating"]>=8)]

Movies_tot=len(filtered_data)

print(Movies_tot)

#What is the median rating of movies directed by Christopher Nolan?

Christopher_Nolan_Movies= df[(df["Director"]=="Christopher Nolan")]

Median_rating=filtered_data[""].med()

print(Median_rating)

#Find the year with the highest average rating?

average_yearly_rating = df.groupby("Year")["Rating"].mean()

Highest_rating= average_yearly_rating.idxmax

print(average_yearly_rating)


#9

Movies_2006_to_2016 = df[(df['Year'] >= 2006) & (df["Year"])]

##%

nun_movies_2006=len(df[df["Year"]==2006])

nun_movies_2006=len(df[df["Year"]==2016])

#% increase 

movies_2006_to_2016 = df[(df['Year'] >= 2006) & (df['Year'] <= 2016)]

# Calculate the number of movies made in 2006 and 2016
num_movies_2006 = len(df[df['Year'] == 2006])
num_movies_2016 = len(df[df['Year'] == 2016])

# Calculate the percentage increase
percentage_increase = ((num_movies_2016-num_movies_2006)/num_movies_2006) * 100
print(percentage_increase)


#10 

import pandas 
from collections import Counter

# Combine all actors into a single list
all_actors = [actor.strip() for actors_list in df['Actors'].str.split(',') for actor in actors_list]

# Find the most common actor
most_common_actor, _ = Counter(all_actors).most_common(1)[0]

print(f'The most common actor in all movies is: {most_common_actor}')

# 11

# genres into a single list
all_genres = [genre.strip() for genres_list in df['Genre'].str.split(',') for genre in genres_list]

# Find unique genres
unique_genres_count = len(set(all_genres))

print(f'The number of unique genres in the dataset is: {unique_genres_count}')


#12 correlation analysis on numerical features
correlation_matrix = df[['Runtime (Minutes)', 'Votes', 'Revenue (Millions)', 'Metascore']].corr()

# Print correlation matrix
print(correlation_matrix)






