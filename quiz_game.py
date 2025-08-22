from question_bank import questions

def run_quiz():
    score = 0
    print("Welcome to the Quiz! Answer the following questions:\n")
    for question, correct_answer in questions.items():
        answer = input(question + " ")
        if answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
        print()  # blank line for readability
    print(f"Your final score is {score} out of {len(questions)}")

if __name__ == "__main__":
    run_quiz()
