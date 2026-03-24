print("Script started")

import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print("Base dir:", BASE_DIR)

csv_path = BASE_DIR / "data" / "raw" / "sales_data.csv"
print("CSV path:", csv_path)

db_path = BASE_DIR / "database" / "sales.db"
print("DB path:", db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER,
    customer TEXT,
    country TEXT,
    amount INTEGER,
    order_date TEXT
)
""")

with open(csv_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            amount = int(row["amount"])
        except (ValueError, TypeError):
            amount = 0

        cursor.execute("""
        INSERT INTO sales (order_id, customer, country, amount, order_date)
        VALUES (?, ?, ?, ?, ?)
        """, (
            int(row["order_id"]),
            row["customer"],
            row["country"],
            amount,
            row["order_date"]
        ))

conn.commit()
conn.close()

print("Data loaded successfully into sales.db")