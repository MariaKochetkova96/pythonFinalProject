import pandas as pd
df = pd.read_csv("Highest Holywood Grossing Movies.csv")
del df['Index']


print(df.columns)
print(df.head(10))

# my_movies = df.to_dict("records")
# print(my_movies[:10])