from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""Summarize the educational text below for a student.

Requirements:
- Keep the main facts and important relationships.
- Remove repetition and unnecessary detail.
- Use simple language.
- Prefer short paragraphs and bullet points when appropriate.
- Do not add facts that are not present in the source.

Text:
{text}"""
    return generate_text(prompt)
