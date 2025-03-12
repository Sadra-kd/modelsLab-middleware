import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Your Modelslab API key, for use in authentication by the proxy itself.
    MODELSLAB_API_KEY: str = os.getenv("MODELSLAB_API_KEY")

settings = Settings()
