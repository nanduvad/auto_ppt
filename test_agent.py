from huggingface_hub import InferenceClient
import os

client = InferenceClient(
    model="google/flan-t5-small",
    token=os.getenv("HF_TOKEN")
)

try:
    response = client.text_generation(
        "Explain Artificial Intelligence in one sentence.",
        max_new_tokens=50
    )

    print("✅ LLM WORKING")
    print("Response:", response)

except Exception as e:
    print("❌ LLM FAILED")
    print("Error:", str(e))