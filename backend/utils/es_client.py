from elasticsearch import Elasticsearch
import os

ES_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")


def get_es_client():
    es = Elasticsearch(ES_URL)
    err_msg = f"Could not connect to Elasticsearch at {ES_URL}"
    if not es.ping():
        raise ConnectionError(err_msg)

    return es
