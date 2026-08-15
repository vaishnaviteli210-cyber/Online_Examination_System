from document_reader import extract_text
from generate_and_save import generate_and_save


file_path = input("Enter document path: ")

document_text = extract_text(file_path)

if not document_text:
    print("Could not read document.")
    exit()


number_of_questions = int(
    input("How many questions? ")
)


print("\nQuestion type:")
print("1. MCQ")
print("2. Theory")
print("3. Both")

choice = input("Choose: ")

question_type_map = {
    "1": "MCQ",
    "2": "Theory",
    "3": "Both"
}

question_type = question_type_map.get(choice)

if not question_type:
    print("Invalid question type.")
    exit()


print("\nDifficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty_choice = input("Choose: ")

difficulty_map = {
    "1": "Easy",
    "2": "Medium",
    "3": "Hard"
}

difficulty = difficulty_map.get(difficulty_choice)

if not difficulty:
    print("Invalid difficulty.")
    exit()


saved_ids = generate_and_save(
    document_text=document_text,
    number_of_questions=number_of_questions,
    difficulty=difficulty,
    question_type=question_type
)

if saved_ids:
    print("\nSaved question IDs:")
    print(saved_ids)
else:
    print("\nNo questions were saved.")