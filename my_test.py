import pytest
import pandas as pd
df = pd.read_csv("C:\\Users\\Mariia\\Desktop\\Python2\\pythonProject\\Highest Holywood Grossing Movies.csv")
from final_project import find_movies_by_genre


def test_find_movies_by_genre(capsys):
    user_input = "Action"
    expected_output = "Random movies of the 'Action' genre:"

    input_mock = lambda: user_input

    find_movies_by_genre(input_mock)

    captured = capsys.readouterr()
    actual_output = captured.out.strip()

    assert actual_output == expected_output