from utils.es_client import get_es_client


def search_movies(
    query: str,
    genre: str = None,
    sort: str = "relevance",
    page: int = 1,
    size: int = 10,
):
    es = get_es_client()
    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "multi_match": {
                            "query": query,
                            "fields": ["title^2", "overview"],
                        }
                    }
                ]
            }
        },
        "from": (page - 1) * size,
        "size": size,
    }

    # Optional genre filter
    if genre:
        body["query"]["bool"]["filter"] = [{"term": {"genre": genre}}]

    # Sorting
    if sort == "rating":
        body["sort"] = [{"rating": {"order": "desc"}}]

    res = es.search(index="movies", body=body)
    results = [
        {
            "title": hit["_source"]["title"],
            "overview": hit["_source"]["overview"],
            "genre": hit["_source"]["genre"],
            "release_date": hit["_source"]["release_date"],
            "rating": hit["_source"]["rating"],
            "score": hit["_score"],
        }
        for hit in res["hits"]["hits"]
    ]
    return {"total": res["hits"]["total"]["value"], "results": results}
