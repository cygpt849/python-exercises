# csv_utils.py
import pandas as pd
from pathlib import Path

DATA_PATH = Path("./data/people.csv")

def load_people_csv(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the people dataset from CSV."""
    return pd.read_csv(path)

def average_age(df: pd.DataFrame) -> float:
    """Compute average age."""
    return df["age"].mean()

def people_in_city(df: pd.DataFrame, city: str) -> pd.DataFrame:
    """Return subset of people living in a given city."""
    return df[df["city"] == city]