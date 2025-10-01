# hello_data.py
import pandas as pd

def main() -> None:
    """Load a tiny dataset and compute a simple statistic."""
    # Create a mini dataset inline (no external file needed yet)
    data = {
        "name": ["Alice", "Bob", "Charlie", "Diana"],
        "age": [25, 32, 37, 29],
    }
    df = pd.DataFrame(data)

    # Print preview
    print("Dataset:\n", df)

    # Compute mean age
    mean_age = df["age"].mean()
    print(f"\nAverage age: {mean_age:.1f}")

if __name__ == "__main__":
    main()
