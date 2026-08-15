VALID_ANSWERS = {"A", "B", "C", "D"}
VALID_DIFFICULTIES = {"Easy", "Medium", "Hard"}
VALID_TYPES = {"MCQ", "Theory"}


def validate_question(question_data):

    # Basic fields
    if "question" not in question_data:
        return False, "Missing field: question"

    if not question_data["question"].strip():
        return False, "Question cannot be empty"

    # Difficulty
    if "difficulty" not in question_data:
        return False, "Missing field: difficulty"

    difficulty = question_data["difficulty"].capitalize()

    if difficulty not in VALID_DIFFICULTIES:
        return False, "Difficulty must be Easy, Medium or Hard"

    # Question type
    question_type = question_data.get("question_type", "MCQ")

    if question_type not in VALID_TYPES:
        return False, "Question type must be MCQ or Theory"

    # -------------------------
    # MCQ validation
    # -------------------------
    if question_type == "MCQ":

        required_fields = [
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "correct_answer"
        ]

        for field in required_fields:
            if field not in question_data:
                return False, f"Missing field: {field}"

        options = [
            question_data["option_a"],
            question_data["option_b"],
            question_data["option_c"],
            question_data["option_d"]
        ]

        for option in options:
            if not option or not option.strip():
                return False, "MCQ options cannot be empty"

        correct_answer = question_data["correct_answer"].upper()

        if correct_answer not in VALID_ANSWERS:
            return False, "Correct answer must be A, B, C or D"

    # -------------------------
    # Theory validation
    # -------------------------
    elif question_type == "Theory":

        theory_answer = question_data.get("theory_answer")

        if not theory_answer or not theory_answer.strip():
            return False, "Theory answer cannot be empty"

    return True, "Question is valid"