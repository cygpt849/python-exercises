from cleaning_utils import load_and_clean

if __name__ == "__main__":
    df = load_and_clean()
    print("Cleaned dataset:\n", df)
    print("\nData types:\n", df.dtypes)
