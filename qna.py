from gemini_client import generate_text

SYSTEM = """You are EduGenie, a student-friendly educational assistant.
Answer accurately and concisely. Explain unfamiliar terms in simple language.
If the question is ambiguous, state the assumption you are making.
Do not pretend to know information you are unsure about."""


def answer_question(question: str) -> str:
    prompt = f"""Answer the student's question.

Question:
{question}

Give a clear answer first, followed by a short explanation or example when useful."""
    return generate_text(prompt, system_instruction=SYSTEM)
