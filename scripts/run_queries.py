import sqlite3
import csv
from pathlib import Path

# Definir rutas
BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR / "database" / "sales.db"
queries_path = BASE_DIR / "sql" / "queries.sql"
output_dir = BASE_DIR / "sql"

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Leer archivo queries.sql
with open(queries_path, "r", encoding="utf-8") as f:
    queries = f.read().split(";")

# Ejecutar cada query y guardar resultado en CSV
for i, query in enumerate(queries):
    query = query.strip()
    if query:
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        output_file = output_dir / f"query_{i}.csv"

        with open(output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            writer.writerows(results)

        print(f"Saved {output_file}")

conn.close()