import psycopg2
from psycopg2 import OperationalError

def check_postgres_connection(host, port, user, password, database):
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        cursor = connection.cursor()

        cursor.execute("SELECT version();")

        result = cursor.fetchone()
        print("Connection to PostgreSQL successful:")
        print(result)

        cursor.close()
        connection.close()

    except OperationalError as e:
        print(f"Error: {e}")

host = "localhost"
port = "5432"
user = "amir"
password = "2002"
database = "test_mohaymen"

check_postgres_connection(host, port, user, password, database)
