from document_reader import extract_text
from gemini_generator import generate_questions


file_path = input("Enter document path: ")

document_text = extract_text(file_path)

if not document_text:
    print("Could not read document.")
    exit()


number = int(input("How many questions? "))

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


print("\nGenerating questions...")

questions = generate_questions(
    document_text=document_text,
    number_of_questions=number,
    difficulty=difficulty,
    question_type=question_type
)


if not questions:
    print("No questions generated.")
    exit()


print(f"\nGenerated {len(questions)} questions.")

for index, question in enumerate(questions, start=1):

    print("\n----------------------------")
    print(f"Question {index}")
    print("----------------------------")

    print(question["question"])

    if question["question_type"] == "MCQ":
        print("A:", question["option_a"])
        print("B:", question["option_b"])
        print("C:", question["option_c"])
        print("D:", question["option_d"])

    elif question["question_type"] == "Theory":
        print("Write your answer:")
   