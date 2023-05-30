import pytest
import pandas as pd
df = pd.read_csv("C:\\Users\\Mariia\\Desktop\\Python2\\pythonProject\\Highest Holywood Grossing Movies.csv")
from final_project import find_movies_by_genre


def test_find_movies_by_genre(capsys):
    genre_name = 'Action'
    expected_output = "Random movies of the 'Action' genre:"

    find_movies_by_genre(genre_name)

    captured = capsys.readouterr()
    actual_output = captured.out.strip()

    assert actual_output == expected_output