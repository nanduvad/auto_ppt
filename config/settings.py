import os


class Config:
    # Hugging Face model (lightweight + fast)
    MODEL_ID = "google/flan-t5-small"

    # Max tokens for generation
    MAX_TOKENS = 200

    # Secure token (set via environment variable)
    HF_TOKEN = os.getenv("HF_TOKEN")