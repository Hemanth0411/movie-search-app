from elasticsearch import Elasticsearch
import os

ES_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")

def get_es_client():
    es = Elasticsearch(ES_URL)
    if not es.ping():
        raise ConnectionError(f"Could not connect to Elasticsearch at {ES_URL}")
    return es
