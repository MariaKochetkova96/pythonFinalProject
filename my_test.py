import pytest
import pandas as pd
df = pd.read_csv("C:\\Users\\Mariia\\Desktop\\Python2\\pythonProject\\Highest Holywood Grossing Movies.csv")
from final_project import find_movies_by_genre

@pytest.mark.parametrize("genre, expected_output", [
    ("Action", "Random movies of the 'Action' genre:"),
    ("Comedy", "Random movies of the 'Comedy' genre:"),
    ("Nonexistent Genre", "No movies found in the entered genre.")
])
def test_find_movies_by_genre(genre, expected_output, capsys):

    input_values = [genre]
    input_mock = mocker.patch('builtins.input', side_effect=input_values)
    find_movies_by_genre()

    captured = capsys.readouterr()

    assert captured.out.strip() == expected_output
