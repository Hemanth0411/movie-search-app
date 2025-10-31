from flask import Flask, jsonify
import os
from elasticsearch import Elasticsearch

app = Flask(__name__)

ELASTICSEARCH_HOST = os.environ.get("ELASTICSEARCH_HOST", "localhost")

try:
    es = Elasticsearch(hosts=[{"host": ELASTICSEARCH_HOST, "port": 9200, "scheme": "http"}])
    es_info = es.info()
    print("Connected to Elasticsearch!")
    print(es_info)
except Exception as e:
    print(f"Could not connect to Elasticsearch: {e}")
    es = None

@app.route('/')
def index():
    """
    A simple health check endpoint.
    """
    return jsonify({
        "status": "ok",
        "message": "Welcome to the Movie Search App!"
    })

@app.route('/es-status')
def es_status():
    """
    Endpoint to check the status of the Elasticsearch connection.
    """
    if es and es.ping():
        return jsonify({
            "status": "ok",
            "message": "Elasticsearch is connected."
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Could not connect to Elasticsearch."
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)