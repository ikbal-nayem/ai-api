import requests
from config import WEB_SEARCH_TOKEN

search_url = "https://ollama.com/api/web_search"

def webSearch(query: str)-> list:
    response = requests.post(
        search_url,
        json={"query": query},
        headers={"Authorization": f"Bearer {WEB_SEARCH_TOKEN}"}
    )
    if response.status_code == 200:
        return response.json().get("results", [])
    print(f"❌ Web search failed with status code {response.status_code}: {response.text}")
    return []
    