import os
from dotenv import load_dotenv

# Loads the environment variables from the .env file
load_dotenv()

class Settings:

    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_URL= os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_COLLECTION = "production_rag"

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "llama3-8b-8192"
    GROQ_FALLBACK_API_KEY = os.getenv("GROQ_FALLBACK_API_KEY")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


settings = Settings()