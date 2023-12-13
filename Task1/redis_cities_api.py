from flask import Flask, jsonify, request
import redis

app = Flask(__name__)

REDIS_HOST = "172.17.0.2"
REDIS_PORT = 6379
REDIS_DB = 0
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

@app.route('/')
def search_cities():
    key = request.args.get('key')
    if not key:
        return jsonify({'error': 'Key parameter is required'}), 400
    cities_bytes = r.smembers(key)
    if not cities_bytes:
        return jsonify({'error': 'Key not found'}), 404
    cities = [city.decode('utf-8') for city in cities_bytes]
    response = {
        'key': key,
        'cities': cities
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)