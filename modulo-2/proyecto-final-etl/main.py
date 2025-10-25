from prefect import flow
from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load


@flow
def main():
    data = extract()
    data_transform = transform(data)
    load(data_transform)
    
if __name__ == "__main__":
    main()
