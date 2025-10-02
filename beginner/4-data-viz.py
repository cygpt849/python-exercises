import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    df = pd.read_csv("beginner/data/people.csv")

    # Diagnostic
    print(df.columns)
    print(df.index)

    # Histogram of ages
    df["age"].plot(kind="hist", bins=5, title="Age Distribution")
    plt.xlabel("Age")
    plt.savefig("plots/histogram.png")
    plt.clf()

    # Bar chart: average age by city
    df.groupby("city")["age"].mean().plot(kind="bar", title="Average Age by City")
    plt.ylabel("Average Age")
    plt.savefig("plots/bar_chart.png")
    plt.clf()

    # Scatter: Age vs index
    df.reset_index().plot(kind="scatter", x="index", y="age", title="Age Scatter")
    plt.savefig("plots/scatter.png")
    plt.clf()


if __name__ == "__main__":
    import os

    os.makedirs("plots", exist_ok=True)
    main()
