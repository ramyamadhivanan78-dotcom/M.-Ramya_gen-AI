from quiz_schema import QuizResponse
from gemini_client import generate_json


def generate_quiz(text: str) -> QuizResponse:
    prompt = f"""Create exactly 3 multiple-choice questions from the educational
content below.

Rules:
- Each question has exactly 4 options.
- Exactly one option is correct.
- correct_answer must exactly match one of the four option strings.
- Add a short explanation for the correct answer.
- Questions must test understanding of the supplied content.
- Do not add facts unrelated to the content.

Content:
{text}"""

    result = generate_json(prompt, QuizResponse)

    if isinstance(result, QuizResponse):
        return result

    if isinstance(result, dict):
        return QuizResponse.model_validate(result)

    return QuizResponse.model_validate_json(result)
