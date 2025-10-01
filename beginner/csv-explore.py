# csv_explore.py
import pandas as pd

def main() -> None:
    """Load and explore a CSV file with pandas."""
    df = pd.read_csv("data/people.csv")

    print("Preview:\n", df.head(), "\n")

    # Slice column
    print("All ages:", df["age"].tolist())

    # Filter
    london = df[df["city"] == "London"]
    print("\nPeople in London:\n", london)

    # Summary stats
    print("\nAverage age:", df["age"].mean())
    print("Max age:", df["age"].max())
    print("Group by city:\n", df.groupby("city")["age"].mean())

if __name__ == "__main__":
    main()