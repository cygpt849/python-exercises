# csv_explore.py
from csv_utils import load_people_csv, average_age, people_in_city

def main() -> None:
    df = load_people_csv()
    print("Average age:", average_age(df))
    print("\nPeople in London:\n", people_in_city(df, "London"))

if __name__ == "__main__":
    main()