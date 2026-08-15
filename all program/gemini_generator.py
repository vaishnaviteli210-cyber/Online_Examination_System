import json
from google import genai

from config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_questions(
    document_text,
    number_of_questions,
    difficulty,
    question_type
):
    """
    Generate MCQ, Theory, or Both questions
    from the supplied document text.
    """

    if not document_text or not document_text.strip():
        print("Document text is empty.")
        return []

    prompt = f"""
You are an examination question generator.

Generate questions ONLY from the document content provided below.

Requirements:
- Number of questions: {number_of_questions}
- Difficulty: {difficulty}
- Question type: {question_type}

Question type rules:

MCQ:
- Generate multiple-choice questions.
- Each question must have options A, B, C and D.
- Provide the correct answer as A, B, C or D.
- Provide an explanation.

Theory:
- Generate descriptive/theory questions.
- Do not generate MCQ options.
- Provide a model answer.
- Provide an explanation if useful.

Both:
- Generate a mixture of MCQ and Theory questions.
- Approximately half should be MCQ and half should be Theory.

Return ONLY valid JSON.

For MCQ use:
{{
    "question_type": "MCQ",
    "question": "...",
    "option_a": "...",
    "option_b": "...",
    "option_c": "...",
    "option_d": "...",
    "correct_answer": "A",
    "theory_answer": null,
    "explanation": "...",
    "difficulty": "{difficulty}"
}}

For Theory use:
{{
    "question_type": "Theory",
    "question": "...",
    "option_a": null,
    "option_b": null,
    "option_c": null,
    "option_d": null,
    "correct_answer": null,
    "theory_answer": "...",
    "explanation": "...",
    "difficulty": "{difficulty}"
}}

Return a JSON array containing the questions.

DOCUMENT:
{document_text}
"""

    try:
        response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

        response_text = response.text.strip()

        # Remove markdown code fences if Gemini adds them
        if response_text.startswith("```"):
            response_text = response_text.replace("```json", "")
            response_text = response_text.replace("```", "")
            response_text = response_text.strip()

        questions = json.loads(response_text)

        if not isinstance(questions, list):
            print("Gemini did not return a question list.")
            return []

        return questions

    except json.JSONDecodeError:
        print("Gemini returned invalid JSON.")
        return []

    except Exception as e:
        print(f"Gemini generation error: {e}")
        return []