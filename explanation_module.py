from config import LOCAL_EXPLAINER_ENABLED, LOCAL_EXPLAINER_MODEL
from gemini_client import generate_text

_pipeline = None


def _get_local_pipeline():
    global _pipeline
    if _pipeline is None:
        from transformers import pipeline
        _pipeline = pipeline(
            "text2text-generation",
            model=LOCAL_EXPLAINER_MODEL,
            max_new_tokens=220,
        )
    return _pipeline


def _local_explain(topic: str) -> str:
    prompt = (
        "Explain the following topic to a beginner in simple, concise language. "
        "Use a small example if helpful.\n\nTopic: " + topic
    )
    result = _get_local_pipeline()(prompt)
    return result[0]["generated_text"].strip()


def explain_topic(topic: str) -> str:
    if LOCAL_EXPLAINER_ENABLED:
        try:
            return _local_explain(topic)
        except Exception:
            # If the local model is unavailable, keep the application usable.
            pass

    return generate_text(
        f"""Explain this topic to a beginner: {topic}

Use:
- a one-sentence definition,
- 2 to 4 simple points,
- one small example,
- one real-world use.

Avoid unnecessary jargon."""
    )
