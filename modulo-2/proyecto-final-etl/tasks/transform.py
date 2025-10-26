from prefect import task
from config import BASE_URL

@task
def transform(data):
    """Transforms extracted raw data into a structured format."""
    transformed_data = []

    for d in data:
        title = d.get("title")
        link = f"{BASE_URL}{d.get('link', '')}"
        tag = d.get("tag")
        image = d.get("image")
        fuel = d.get("fuel")
        location = d.get("location")
        brand = d.get("brand")
        year = d.get("year")
        advertiser = d.get("advertiser")

        price_raw = d.get("price", "")
        if price_raw and price_raw.lower() != "consultar":
            try:
                price = float(price_raw.replace("US$", "").replace(",", "").strip())
            except ValueError:
                price = None
        else:
            price = None

        transformed_data.append(
            (title, link, tag, image, fuel, location, price, brand, year, advertiser)
        )

    print(f"Transformation completed. Total transformed records: {len(transformed_data)}")
    return transformed_data
