import pandas as pd
from typing import Optional


def load_and_clean(path: str = "beginner/data/messy.csv") -> pd.DataFrame:
    """Load a messy dataset and return a cleaned DataFrame."""
    df = pd.read_csv(path)

    # Normalize column names
    df.columns = [col.strip().lower() for col in df.columns]

    # Convert Age to numeric (force errors to NaN)
    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    # Handle missing values
    df["age"] = df["age"].fillna(df["age"].median())
    df["city"] = df["city"] = df["city"].fillna("Unknown")

    return df
