import os
from prefect import task
import mysql.connector
from dotenv import load_dotenv

load_dotenv() 

@task
def load(data):
    """Loads transformed data into a MySQL database."""
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASS", "password"),
        database=os.getenv("DB_NAME", "db_g5")
    )
    cursor = connection.cursor()

    # Drop existing table and recreate
    cursor.execute("DROP TABLE IF EXISTS tbl_autos;")
    connection.commit()

    cursor.execute("""
        CREATE TABLE tbl_autos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            link TEXT,
            tag TEXT,
            image TEXT,
            fuel VARCHAR(255),
            location VARCHAR(255),
            price DOUBLE,
            brand VARCHAR(255),
            year VARCHAR(255),
            advertiser VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    connection.commit()

    insert_query = """
        INSERT INTO tbl_autos (
            title, link, tag, image, fuel, location, price, brand, year, advertiser
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(insert_query, data)
    connection.commit()

    print(f"Successfully inserted {cursor.rowcount} records into the database.")

    cursor.close()
    connection.close()
    return cursor.rowcount
