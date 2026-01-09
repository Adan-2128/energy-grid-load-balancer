import os
import requests
from pymongo import MongoClient

# Lazy loading — only runs when function is called
def _get_guidelines():
    client = MongoClient(os.getenv("MONGO_URI"))
    return client.energy_db.energy_guidelines.find()

def get_rag_explanation(query):
    try:
        guidelines = list(_get_guidelines())
        ALL_GUIDELINES = "\n".join([doc["text"] for doc in guidelines])
    except:
        ALL_GUIDELINES = "High temperatures increase HVAC usage. Reduce cooling during peak hours to save energy."

    prompt = f"""You are an energy efficiency expert for buildings.
Use only the guidelines below to answer clearly and concisely.

Guidelines:
{ALL_GUIDELINES}

Question: {query}
Answer:"""

    url = "https://eu-de.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-31"
    payload = {
        "model_id": "ibm/granite-3-8b-instruct",
        "project_id": os.getenv("WATSONX_PROJECT_ID"),
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 200,
            "temperature": 0.5
        }
    }
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json"
    }

    try:
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        if r.status_code == 200:
            return r.json()["results"][0]["generated_text"]
        else:
            return f"Warning: Granite API error {r.status_code}. Using fallback advice: Reduce HVAC during hot hours."
    except:
        return "Reduce HVAC by 20% and dim lights to save energy."

def get_token():
    token_url = "https://iam.cloud.ibm.com/identity/token"
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": os.getenv("WATSONX_API_KEY")
    }
    r = requests.post(token_url, data=data)
    r.raise_for_status()
    return r.json()["access_token"]