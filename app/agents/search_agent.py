import arxiv

def search_papers(query: str, max_results: int = 5):
    search = arxiv.Search(query=query, max_results=max_results)
    results = []
    for result in search.results():
        results.append({
            "title": result.title,
            "summary": result.summary,
            "authors": [a.name for a in result.authors],
            "pdf_url": result.pdf_url,
            "published": result.published.isoformat()
        })
    return results
