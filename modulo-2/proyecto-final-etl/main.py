from prefect import flow
from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load


@flow
def main():
    """Main ETL flow to extract, transform, and load car data."""
    data = extract()
    transformed = transform(data)
    print(f"Transformed {len(transformed)} records.")
    inserted = load(transformed)
    print(f"Inserted {inserted} records into the database.")


if __name__ == "__main__":
    main()
