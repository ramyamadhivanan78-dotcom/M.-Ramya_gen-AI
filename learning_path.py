from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""Create a personalized learning path for this topic: {topic}

Structure it from beginner to advanced.
For each stage include:
1. What to learn
2. Why it matters
3. A realistic suggested timeline
4. Practice ideas

Finish with useful resource types such as documentation, videos, articles,
or books. Do not invent exact URLs unless you are certain they exist.
Keep the plan practical for a student."""
    return generate_text(prompt)
