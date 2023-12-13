import csv
import psycopg2
from psycopg2 import sql
import openpyxl

DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "amir"
DB_PASSWORD = "2002"
DB_NAME = "test_mohaymen"

XLSX_FILE_PATH = "REF_SMS/Ref.xlsx"

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)

cursor = conn.cursor()

wb = openpyxl.load_workbook(XLSX_FILE_PATH)
sheet = wb.active
row_iterator = sheet.iter_rows(min_row=2)


data = []
for row in row_iterator:
    pay_type = row[0].value
    value = row[1].value
    data.append((pay_type, value))



create_table_sql = """
CREATE TABLE IF NOT EXISTS paytype (
  pay_type DECIMAL(1, 0) PRIMARY KEY,
  value VARCHAR(50)
);
"""

cursor.execute(create_table_sql)
conn.commit()

insert_data_sql = """
INSERT INTO paytype (pay_type, value) VALUES (%s, %s);
"""

cursor.executemany(insert_data_sql, data)
conn.commit()

cursor.close()
conn.close()

print("Data successfully saved to PostgreSQL database!")
