import pandas as pd
import requests

df = pd.read_csv("C:\\Users\\Mariia\\Desktop\\Python2\\pythonProject\\Highest Holywood Grossing Movies.csv")
df.drop('Index', axis=1, inplace=True)

# Function to search for movies by genre in DF
def find_movies_by_genre(genre_name):
    filtered_movies = df[df.Genre.str.contains(genre_name, case=False)]

    if not filtered_movies.empty:
        random_movies = filtered_movies.sample(n=5)
        print(random_movies[['Title', 'Genre', 'Movie Info']])
    else:
        print("No movies found in the entered genre.")


# Function to search for movie information
def find_movie_info(movie_title):
    filtered_movies = df[df['Title'].str.contains(movie_title, case=False)]

    if filtered_movies.empty:
        print("No movies found for the entered title.")
    else:
        print(filtered_movies[['Title', 'Genre', 'Movie Info']])

# Function to search for similar movies
def find_similar_movies(movie_title):
    filtered_movies = df[df['Title'].str.contains(movie_title, case=False)]

    if filtered_movies.empty:
        print("No movies found for the entered title.")
    else:
        movie_genre = filtered_movies.iloc[0]['Genre']
        similar_movies = df[df['Genre'].str.contains(movie_genre, case=False)]
        similar_movies = similar_movies[similar_movies['Title'] != movie_title].sample(n=5)
        print(similar_movies[['Title', 'Genre', 'Movie Info']])


# Function to search  movies
def find_movie_genre(movie_title):
    filtered_movies = df[df['Title'].str.contains(movie_title, case=False)]

    if filtered_movies.empty:
        print("No movies found for the entered title.")
    else:
        url = f"https://www.google.com/search?q={movie_title}"
        response = requests.get(url)
        print("Movies found:")
        print(filtered_movies[['Title', 'Genre', 'Movie Info']])

if __name__ == '__main__':

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
            user_input = input("Enter the genre of movies you are looking for: ").strip()
            find_movies_by_genre(user_input)
        elif choice == "2":
            user_input = input("Enter the title of the movie you want to find information about: ").strip()
            find_movie_info(user_input)
        elif choice == "3":
            user_input = input("Enter the title of the movie to find similar movies: ").strip()
            find_similar_movies(user_input)
        elif choice == "4":
            user_input = input("Enter the title of the movie you like: ").strip()
            find_movie_genre(user_input)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.\n")

# random_movies.to_csv('Random_movies.csv', index=False)
