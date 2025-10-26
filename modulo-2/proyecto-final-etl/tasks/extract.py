from prefect import task
import requests
from bs4 import BeautifulSoup
import re
import json
from config import NEW_CARS_URL

@task
def extract():
    """Extracts car listings from NeoAuto's website."""
    extracted_data = []

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    response = requests.get(NEW_CARS_URL, headers=headers)

    if response.status_code != 200:
        print("Error fetching main page.")
        return extracted_data

    soup = BeautifulSoup(response.content, "html.parser")

    # Find total number of pages
    last_page_link = soup.find("a", class_="c-pagination-content__last-page")
    match = re.search(r"page=(\d+)", last_page_link["href"]) if last_page_link else None
    total_pages = int(match.group(1)) if match else 1
    print(f"Total number of pages: {total_pages}")

    # Iterate through all pages
    for page in range(1, total_pages + 1):

        page_url = f"{NEW_CARS_URL}?page={page}"
        print(f"Fetching page {page}...")

        response = requests.get(page_url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to load page {page}. Skipping.")
            continue

        soup = BeautifulSoup(response.content, "html.parser")
        car_articles = soup.find_all("article", class_="c-results")

        print(f"Found {len(car_articles)} car listings on page {page}.")

        for article in car_articles:
            
            data_gtm = json.loads(article["data-gtm"])
            title = article.find("h2", class_="c-results__header-title").text.strip()
            link = article.find("a", class_="c-results__link")["href"]
            tag = article.find("div", class_="c-results-tag__stick")
            tag = tag.get_text().strip() if tag else None
            image = article.find("img", class_="c-results-slider__img-inside")["data-src"]
            fuel = article.find("span", class_="c-results-used__detail-fuel").text.strip()
            location = article.find(
                "span", class_="c-results-details__description-text--highlighted"
            ).text.strip()
            price = article.find("div", class_="c-results-mount__price").text.strip()

            extracted_data.append({
                "title": title,
                "link": link,
                "tag": tag,
                "image": image,
                "fuel": fuel,
                "location": location,
                "price": price,
                "brand": data_gtm.get("item_brand"),
                "year": data_gtm.get("item_year"),
                "advertiser": data_gtm.get("item_advertiser"),
            })

    print(f"Extraction completed. Total records: {len(extracted_data)}")
    return extracted_data
