import json
import os
from elasticsearch import Elasticsearch, helpers

ES_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
INDEX_NAME = "movies"

def create_index(es_client):
    with open("mappings/movies_mapping.json", "r") as f:
        mapping = json.load(f)
    if not es_client.indices.exists(index=INDEX_NAME):
        es_client.indices.create(index=INDEX_NAME, body=mapping)
        print(f"✅ Created index: {INDEX_NAME}")
    else:
        print(f"ℹ️ Index '{INDEX_NAME}' already exists")

def ingest_data(es_client):
    with open("data/sample_movies.json", "r") as f:
        docs = json.load(f)
    actions = [
        {"_index": INDEX_NAME, "_source": doc}
        for doc in docs
    ]
    helpers.bulk(es_client, actions)
    print(f"✅ Indexed {len(docs)} movie documents")

if __name__ == "__main__":
    es = Elasticsearch(ES_URL)
    if not es.ping():
        print("❌ Could not connect to Elasticsearch at", ES_URL)
    else:
        print("✅ Connected to Elasticsearch")
        create_index(es)
        ingest_data(es)
