# test_csv_utils.py
import pandas as pd
from csv_utils import load_people_csv, average_age, people_in_city


def test_load_people_csv():
    df = load_people_csv()
    assert not df.empty
    assert set(df.columns) == {"name", "age", "city"}


def test_average_age():
    df = pd.DataFrame({"name": ["A", "B"], "age": [20, 30], "city": ["X", "Y"]})
    assert average_age(df) == 25


def test_people_in_city():
    df = pd.DataFrame({"name": ["A", "B"], "age": [20, 30], "city": ["X", "X"]})
    subset = people_in_city(df, "X")
    assert len(subset) == 2
