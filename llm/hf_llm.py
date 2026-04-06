import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json",
}


def generate(prompt: str) -> str:
    """
    Generate text using HuggingFace cloud LLM
    """

    payload = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {"role": "system", "content": "You are an expert presentation creator."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 800,
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    # ---------- ERROR HANDLING ----------
    if response.status_code != 200:
        raise Exception(
            f"HF API Error {response.status_code}: {response.text}"
        )

    data = response.json()

    try:
        content = data["choices"][0]["message"]["content"]
    except Exception:
        raise Exception(f"Invalid HF response: {data}")

    # Prevent API error text becoming PPT content
    if "error" in content.lower():
        raise Exception("LLM returned error instead of content")

    return content.strip()