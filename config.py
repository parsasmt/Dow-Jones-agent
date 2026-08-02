import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")

    MODEL_NAME = os.getenv("MODEL_NAME")

    DATABASE_URL = os.getenv("DATABASE_URL")

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    FRED_API_KEY = os.getenv("FRED_API_KEY")
    


config = Config()