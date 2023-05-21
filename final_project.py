import pandas as pd
import requests

df = pd.read_csv("Highest Holywood Grossing Movies.csv")
del df['Index']
desired_genres = input("Hi! What movie did you want to watch today? Enter the genre: ")

filtered_movies = df[df.Genre.str.contains(desired_genres)]
if desired_genres in filtered_movies:     # When user know genre
    random_movies = filtered_movies.sample(n=10)
    print(random_movies[['Title', 'Genre', 'Movie Info']])

else: # Ask the user to enter the name of a movie they like
    movie_title = input("Enter the name of a movie you like: ")
    filtered_movies = df[df['Title'].str.contains(movie_title, case=False)]

    if filtered_movies.empty:
        print("No movies found for the entered title.")
    else:
        # Display the matched movies
        url = f"https://www.google.com/search?q={movie_name}"
        response = requests.get(url)
        print("Movies found:")
        print(filtered_movies[['Title', 'Genre', 'Movie Info']])


# random_movies.to_csv('Random_movies.csv', index=False)




# print(df.columns)
# print(df.Genre)
# print(df.head(10))
# print(df.tail(10))
# my_movies = df.to_dict("records")
# print(my_movies[:10])