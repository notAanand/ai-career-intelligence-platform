from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    PROJECT_NAME = "CareerPilot AI"

    VERSION = "1.0.0"

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    GEMINI_MODEL = os.getenv(
        "MODEL_NAME",
        "gemini-2.5-flash"
    )


settings = Settings()