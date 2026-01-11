import re
import ollama
import json

from openai import OpenAI
from config import INFERENCE_BASE_URL, MODEL, OR_TOKEN
from web_search import webSearch
from template import prompt

OUTPUT_FILE = "bangladesh_holidays_2026.json"

client = OpenAI(base_url=INFERENCE_BASE_URL, api_key=OR_TOKEN)

def get_holidays_json():
    print(f"🔍 Searching the web for 2026 Bangladesh holidays...")
    
    # 1. Perform the Web Search using Ollama's native tool
    # This returns a list of result objects with title, description, and url
    search_query = "public government holidays list Bangladesh 2026 dates"
    search_results = webSearch(search_query)

    # Convert search results to a string context for the LLM
    context_text = "\n".join(
        [f"Source: {r.get("title")}\nContent: {r.get("content")}\nURL: {r.get("url")}" for r in search_results]
    )

    print("✅ Search complete. Processing data with Ollama...")

    # response = ollama.chat(
    #     model=MODEL,
    #     messages=[{'role': 'user', 'content': prompt + "\n" + context_text}],
    #     format="json",
    #     stream=False
    # )
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
        # Validate JSON by parsing it
        data = {}
        if json_match:
            json_string = json_match.group(0)
            data = json.loads(json_string)
        
        # Write to file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        print(f"🎉 Success! Holidays saved to '{OUTPUT_FILE}'")
        print(json.dumps(data, indent=2))
        
    except json.JSONDecodeError as e:
        print("❌ Error: The model did not produce valid JSON. Here is the raw output:", e)
        print(content)

if __name__ == "__main__":
    get_holidays_json()