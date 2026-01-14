import datetime
import re
import json

from openai import OpenAI
from config import INFERENCE_BASE_URL, MODEL, OR_TOKEN
from services.web_search import webSearch
from template import prompt

client = OpenAI(base_url=INFERENCE_BASE_URL, api_key=OR_TOKEN)

def getHolidaysJSON(year: int):
    print(f"🔍 Searching the web for {year} Bangladesh holidays...")
    
    search_query = f"public government holidays list for '{year}' in Bangladesh. get most recent and accurate information from government websites and official sources."
    search_results = webSearch(search_query)

    context_text = "\n".join(
        [f"Source: {r.get("title")}\nContent: {r.get("content")}\nURL: {r.get("url")}" for r in search_results]
    )
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{'role': 'user', 'content': prompt + "\n" + context_text}],
        stream=False
    )

    content = response.choices[0].message.content

    if content is None:
        print("❌ Error: No content received from the model.")
        return
    
    json_match = re.search(r'\{.*\}', content, re.DOTALL)

    try:
        data = {}
        if json_match:
            json_string = json_match.group(0)
            data = json.loads(json_string)
        
        print(f"🎉 Success!", data)
        return {**data, "year": year, "sources": [res.get("url") for res in search_results]}
        
    except json.JSONDecodeError as e:
        print("❌ Error: The model did not produce valid JSON. Here is the raw output:", e)
        print(content)

if __name__ == "__main__":
    getHolidaysJSON(datetime.datetime.now().year)