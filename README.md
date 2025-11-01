# Movie Search (mini)

Small demo showing Elasticsearch full-text search with a minimal FastAPI backend.

## Goals
- Learn Elasticsearch indexing, multi-field search, scoring, and highlighting.
- Minimal, reproducible, Dockerized setup.

## Quick start
1. `docker compose up -d`
2. `cd backend && docker build -t movie-backend . && docker run --rm -p 8000:8000 movie-backend`

## 🧩 Ingest Sample Data

To load a small movie dataset into Elasticsearch:

```bash
docker compose up -d
python scripts/ingest_sample.py
```
Then verify

```bash
curl -s http://localhost:9200/movies/_count
```
You should see a count of 5 documents.

## 🔍 Search API

After ingesting data, test the search API:

```bash
curl "http://localhost:8000/search?q=inception"
curl "http://localhost:8000/search?q=batman&genre=Action&sort=rating&page=1&size=2"
 ```

Response Example:
```JSON
{
  "total": 1,
  "results": [
    {
      "title": "Inception",
      "overview": "...",
      "genre": "Sci-Fi",
      "release_date": "2010-07-16",
      "rating": 8.8,
      "score": 3.21
    }
  ]
}
```

(Full instructions to be added in later steps)
