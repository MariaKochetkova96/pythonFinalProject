import pandas as pd
import requests


df = pd.read_csv("Highest Holywood Grossing Movies.csv")
df.drop('Index', axis=1, inplace=True)

# desired_genres = input("Hi! What movie did you want to watch today? Enter the genre: ")
#
# filtered_movies = df[df.Genre.str.contains(desired_genres)]
# if not filtered_movies.empty:    # When user know genre
#     random_movies = filtered_movies.sample(n=10)
#     print(random_movies[['Title', 'Genre', 'Movie Info']])
#
# else:   # df.empty  Ask the user to enter the name of a movie they like
#     movie_title = input("Enter the name of a movie you like: ").strip()
#     filtered_movies = df[df['Title'].str.contains(movie_title, case=False)]
#
#     if filtered_movies.empty:
#         print("No movies found for the entered title.")
#     else:
#         # Display the matched movies
#         url = f"https://www.google.com/search?q={movie_title}"
#         response = requests.get(url)
#         print("Movies found:")
#         print(filtered_movies[['Title', 'Genre', 'Movie Info']])


# Function to search for movies by genre
def search_movies_by_genre():
    user_input = genre_entry.get().strip()
    filtered_movies = df[df.Genre.str.contains(user_input, case=False)]

    if not filtered_movies.empty:
        result_text.set(filtered_movies[['Title', 'Genre', 'Movie Info']])
    else:
        result_text.set("No movies found in the entered genre.")


# Function to search for movie information
def search_movie_info():
    movie_title = title_entry.get().strip()
    filtered_movies = df[df['Title'].str.contains(movie_title, case=False)]

    if filtered_movies.empty:
        result_text.set("No movies found for the entered title.")
    else:
        url = f"https://www.google.com/search?q={movie_title}"
        response = requests.get(url)
        result_text.set(filtered_movies[['Title', 'Genre', 'Movie Info']])

# Function to search for similar movies
def search_similar_movies():
    movie_title = title_entry.get().strip()
    filtered_movies = df[df['Title'].str.contains(movie_title, case=False)]

    if filtered_movies.empty:
        result_text.set("No movies found for the entered title.")
    else:
        similar_movies = filtered_movies.sample(n=5)
        result_text.set(similar_movies[['Title', 'Genre', 'Movie Info']])


# random_movies.to_csv('Random_movies.csv', index=False)


# print(df.head(10))
# print(df.tail(10))
# my_movies = df.to_dict("records")
# print(my_movies[:10])