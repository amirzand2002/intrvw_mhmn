import csv
import psycopg2
from psycopg2 import sql
import openpyxl
import pandas as pd

DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "amir"
DB_PASSWORD = "2002"
DB_NAME = "test_mohaymen"

CSV_FILE_PATH = "REF_SMS/REF_CBS_SMS2.csv"
file = pd.read_csv(CSV_FILE_PATH)

columns = {
    "ROAMSTATE_519": "SMALLINT",
    "CUST_LOCAL_START_DATE_15": "BIGINT",
    "CDR_ID_1": "BIGINT",
    "CDR_SUB_ID_2": "SMALLINT",
    "CDR_TYPE_3": "CHAR",
    "SPLIT_CDR_REASON_4": "CHAR",
    "RECORD_DATE": "TIMESTAMP",
    "PAYTYPE_515": "SMALLINT",
    "DEBIT_AMOUNT_42": "BIGINT",
    "SERVICEFLOW_498": "SMALLINT",
    "EVENTSOURCE_CATE_17": "CHAR",
    "USAGE_SERVICE_TYPE_19": "SMALLINT",
    "SPECIALNUMBERINDICATOR_534": "SMALLINT",
    "BE_ID_30": "SMALLINT",
    "CALLEDPARTYIMSI_495": "VARCHAR(255) DEFAULT NULL",
    "CALLINGPARTYIMSI_494": "BIGINT",
}

table_name = "REF_CBS_SMS2"

try:
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)

cursor = conn.cursor()

create_table_sql = sql.SQL(
    "CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
).format(
    table_name=sql.Identifier(table_name),
    columns=sql.SQL(", ").join(
        [sql.SQL("{column} {datatype}").format(column=sql.Identifier(col), datatype=sql.SQL(columns[col])) for col in columns]
    ),
)
cursor.execute(create_table_sql)

for index, row in file.iterrows():
    insert_data_sql = sql.SQL(
        "INSERT INTO {table_name} ({columns}) VALUES ({values});"
    ).format(
        table_name=sql.Identifier(table_name),
        columns=sql.SQL(", ").join(sql.Identifier(col) for col in columns),
        values=sql.SQL(", ").join(sql.Literal(row[col]) for col in columns),
    )
    cursor.execute(insert_data_sql)

conn.commit()
cursor.close()
conn.close()
