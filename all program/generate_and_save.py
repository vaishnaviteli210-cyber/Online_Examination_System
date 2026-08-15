from gemini_generator import generate_questions
from question_generator import save_question


def generate_and_save(
    document_text,
    number_of_questions,
    difficulty,
    question_type
):
    """
    Generate questions using Gemini,
    validate them, and save them to MySQL.
    """

    print("\nGenerating questions with Gemini...")

    questions = generate_questions(
        document_text=document_text,
        number_of_questions=number_of_questions,
        difficulty=difficulty,
        question_type=question_type
    )

    if not questions:
        print("No questions generated.")
        return []

    saved_question_ids = []

    for index, question in enumerate(questions, start=1):

        print(f"\nProcessing question {index}...")

        question_id = save_question(question)

        if question_id:
            saved_question_ids.append(question_id)
        else:
            print(f"Question {index} was not saved.")

    print("\n==============================")
    print("Question generation completed.")
    print("Questions generated:", len(questions))
    print("Questions saved:", len(saved_question_ids))
    print("==============================")

    return saved_question_ids