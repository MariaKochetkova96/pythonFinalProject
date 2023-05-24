import pandas as pd
import requests

df = pd.read_csv("Highest Holywood Grossing Movies.csv")
df.drop('Index', axis=1, inplace=True)

OMDB_API_KEY = "YOUR_OMDB_API_KEY"

# Function to search for movies by genre in DF
def find_movies_by_genre():
    user_input = input("Enter the genre of movies you are looking for: ").strip()
    filtered_movies = df[df.Genre.str.contains(user_input, case=False)]

    if not filtered_movies.empty:
        random_movies = filtered_movies.sample(n=5)
        print(random_movies[['Title', 'Genre', 'Movie Info']])
        # print(filtered_movies[['Title', 'Genre', 'Movie Info']])
    else:
        print("No movies found in the entered genre.")


# Function to search for movie information
def find_movie_info():
    movie_title = input("Enter the title of the movie you want to find information about: ").strip()
    filtered_movies = df[df['Title'].str.contains(movie_title, case=False)]

    if filtered_movies.empty:
        print("No movies found for the entered title.")
    else:
        print(filtered_movies[['Title', 'Genre', 'Movie Info']])

# Function to search for similar movies
def find_similar_movies():
    movie_title = input("Enter the title of the movie to find similar movies: ").strip()
    filtered_movies = df[df['Title'].str.contains(movie_title, case=False)]

    if filtered_movies.empty:
        print("No movies found for the entered title.")
    else:
        movie_genre = filtered_movies.iloc[0]['Genre']
        similar_movies = df[df['Genre'].str.contains(movie_genre, case=False)]
        similar_movies = similar_movies[similar_movies['Title'] != movie_title].sample(n=5)
        print(similar_movies[['Title', 'Genre', 'Movie Info']])


# Function to search  movies
def find_movie_genre():
    movie_title = input("Enter the title of the movie you like: ").strip()
    filtered_movies = df[df['Title'].str.contains(movie_title, case=False)]

    if filtered_movies.empty:
        print("No movies found for the entered title.")
    else:
        movie_title = filtered_movies.iloc[0]['Title']
        url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={movie_title}"
        response = requests.get(url)
        data = response.json()

        if 'Genre' in data:
            print(f"The genre of the movie '{movie_title}' is: {data['Genre']}")
        else:
            print("Genre information not found for the movie.")

# Main program loop
while True:
    print("Please choose an option:")
    print("1. Find movies by genre")
    print("2. Find movie information")
    print("3. Find similar movies")
    print("4. Find movie genre")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        find_movies_by_genre()
    elif choice == "2":
        find_movie_info()
    elif choice == "3":
        find_similar_movies()
    elif choice == "4":
        find_movie_genre()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.\n")

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





# random_movies.to_csv('Random_movies.csv', index=False)


# print(df.head(10))
# print(df.tail(10))
# my_movies = df.to_dict("records")
# print(my_movies[:10])