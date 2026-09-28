import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
LOCAL_EXPLAINER_ENABLED = os.getenv("LOCAL_EXPLAINER_ENABLED", "false").lower() == "true"
LOCAL_EXPLAINER_MODEL = os.getenv(
    "LOCAL_EXPLAINER_MODEL", "MBZUAI/LaMini-Flan-T5-783M"
)

MAX_INPUT_CHARS = int(os.getenv("MAX_INPUT_CHARS", "12000"))
