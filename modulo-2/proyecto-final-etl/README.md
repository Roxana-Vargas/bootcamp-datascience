# 🚗 ETL Project – NeoAuto Data Pipeline

ETL (**Extract, Transform, Load**) pipeline developed in **Python** to extract, transform, and load vehicle data from [NeoAuto](https://neoauto.com).

---

## 👩‍💻 Author

**Olinda Vargas**

---

## ⚙️ Setup Instructions

### 🧩 Step 1 – Create a virtual environment

```bash
python -m venv venv
```

### ▶️ Step 2 – Activate the virtual environment

```bash
# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

### 📦 Step 3 – Install dependencies

```bash
pip install -r requirements.txt
```

### 🚀 Step 4 – Run the project

```bash
python main.py
```

---

## 📁 Project Structure

```
ETL-PROJECT/
├── tasks/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🧠 Overview

* **Extract:** Retrieves data from NeoAuto through web scraping.
* **Transform:** Cleans, normalizes, and structures the extracted data.
* **Load:** Inserts the processed data into a **MySQL** database.

---

## 💡 Prerequisites

* **Python 3.10 or higher**
* **MySQL** installed and running
* `.env` file configured with your database credentials:

```bash
DB_HOST=localhost
DB_USER=user
DB_PASS=password
DB_NAME=db_g5
```

---

## 🧰 Main Dependencies

This project uses the following Python libraries:

* [Prefect](https://www.prefect.io/) – Workflow orchestration
* [Requests](https://requests.readthedocs.io/) – HTTP requests handling
* [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/) – HTML parsing
* [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) – MySQL connection
* [python-dotenv](https://pypi.org/project/python-dotenv/) – Environment variables management

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---
