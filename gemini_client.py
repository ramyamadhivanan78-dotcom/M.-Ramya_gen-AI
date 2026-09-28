from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODEL, MAX_INPUT_CHARS

_client = None


def get_client():
    global _client

    if not GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Copy .env.example to .env and add your Google Gemini API key."
        )

    if _client is None:
        _client = genai.Client(api_key=GEMINI_API_KEY)

    return _client


def generate_text(prompt: str, *, system_instruction: str | None = None) -> str:
    if not prompt.strip():
        raise ValueError("Input cannot be empty.")

    prompt = prompt[:MAX_INPUT_CHARS]

    config_kwargs = {
        "temperature": 0.3,
        "max_output_tokens": 1500,
    }

    if system_instruction:
        config_kwargs["system_instruction"] = system_instruction

    response = get_client().models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(**config_kwargs),
    )

    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned an empty response.")

    return text.strip()


def generate_json(prompt: str, schema):
    prompt = prompt[:MAX_INPUT_CHARS]

    response = get_client().models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=1800,
            response_mime_type="application/json",
            response_schema=schema,
        ),
    )

    if getattr(response, "parsed", None) is not None:
        return response.parsed

    text = getattr(response, "text", None)
    if not text:
        raise RuntimeError("Gemini returned no structured response.")

    return text
