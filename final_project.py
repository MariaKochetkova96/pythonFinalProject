import pandas as pd

df = pd.read_csv("Highest Holywood Grossing Movies.csv")
del df['Index']
desired_genres = input("Hi! What movie did you want to watch today? Enter the genre: ")
filtered_movies = df[df.Genre.str.contains(desired_genres)]
random_movies = filtered_movies.sample(n=10)
print(random_movies[['Title', 'Genre', 'Movie Info']])

random_movies.to_csv('Random_movies.csv', index=False)




# print(df.columns)
# print(df.Genre)
# print(df.head(10))
# print(df.tail(10))
# my_movies = df.to_dict("records")
# print(my_movies[:10])