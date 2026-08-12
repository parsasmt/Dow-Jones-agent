import os
from dotenv import load_dotenv

load_dotenv()


def get_config_value(name: str, default=None):
    """
    Get configuration value from:
    1. Environment variables / .env
    2. Streamlit Secrets
    3. Default value
    """

    # First: local environment / .env
    value = os.getenv(name)

    if value:
        return value

    # Second: Streamlit Cloud Secrets
    try:
        import streamlit as st

        value = st.secrets.get(name)

        if value:
            return value

    except Exception:
        # Streamlit may not be available when running
        # the project outside Streamlit.
        pass

    return default


class Config:

    # --------------------------------------------------
    # OpenRouter
    # --------------------------------------------------

    OPENROUTER_API_KEY = get_config_value(
        "OPENROUTER_API_KEY"
    )

    OPENROUTER_BASE_URL = get_config_value(
        "OPENROUTER_BASE_URL",
        "https://openrouter.ai/api/v1"
    )

    MODEL_NAME = get_config_value(
        "MODEL_NAME",
        "openai/gpt-oss-20b:free"
    )

    # --------------------------------------------------
    # Database
    # --------------------------------------------------

    DATABASE_URL = get_config_value(
        "DATABASE_URL",
        "sqlite:///dow_jones.db"
    )

    # --------------------------------------------------
    # External APIs
    # --------------------------------------------------

    TAVILY_API_KEY = get_config_value(
        "TAVILY_API_KEY"
    )

    FRED_API_KEY = get_config_value(
        "FRED_API_KEY"
    )


config = Config()