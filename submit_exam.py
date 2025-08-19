def submit_exam(student_name, **answers):
    print(f"\nExam submitted by: {student_name}")
    for q, ans in answers.items():
        print(f"{q}: {ans}")

# --- User Input ---
name = input("Enter student name: ")

num_questions = int(input("How many questions to submit? "))

answers = {}
for i in range(1, num_questions + 1):
    question = f"Q{i}"
    answer = input(f"Enter answer for {question}: ")
    answers[question] = answer

submit_exam(name, **answers)
