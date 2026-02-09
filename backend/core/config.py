import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME")

settings = Settings()
