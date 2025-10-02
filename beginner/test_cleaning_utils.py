import pandas as pd
from cleaning_utils import load_and_clean


def test_no_missing_values(tmp_path):
    # Copy messy.csv to tmp folder
    test_csv = tmp_path / "messy.csv"
    test_csv.write_text("Name,Age,City\nA,25,Paris\nB,,London")

    df = load_and_clean(str(test_csv))

    # Check schema
    assert set(df.columns) == {"name", "age", "city"}
    # Ensure no NaNs remain
    assert not df.isnull().any().any()
    # Ensure age is numeric
    assert pd.api.types.is_numeric_dtype(df["age"])
