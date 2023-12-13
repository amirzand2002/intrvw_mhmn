import csv
import redis

REDIS_HOST = "172.17.0.2"
REDIS_PORT = 6379
REDIS_DB = 0
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

CSV_FILE_PATH = "Task1/Cities/CountryCode-City.csv"


with open(CSV_FILE_PATH, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        country_code = row[0]
        city = row[1]
        key = country_code
        r.sadd(key, city)

r.close()
print("City list added to Redis")
