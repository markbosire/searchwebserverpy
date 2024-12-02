from fastapi import FastAPI, HTTPException, Query
from googlesearch import search

app = FastAPI()

@app.get("/search")
async def perform_search(
    query: str = Query(..., description="Search query string"),
    sleep_interval: float = Query(5.0, description="Time to wait between requests in seconds"),
    num_results: int = Query(200, description="Number of results to fetch (max 200)")
):
    
    if num_results > 200 or num_results <= 0:
        raise HTTPException(status_code=400, detail="num_results must be between 1 and 200")
    try:
        results = []
        for url in search(query, num_results=num_results, sleep_interval=sleep_interval):
            results.append(url)
        return {"query": query, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the server with: uvicorn filename:app --reload

