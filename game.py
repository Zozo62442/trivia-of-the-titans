from api import get_questions
from utile import validate_answer, show_final_results, clear_screen
import time


def start_quiz(username):
    """
    Runs the main quiz game loop.
    """
    clear_screen()
    print(f"Welcome to Trivia of Titans {username}! \n")
    print("You'll be asked 10 mythology questions. Choose the correct answer by typing A, B, C, or D (it is case sensitive)!\n")
    time.sleep(2)

    questions = get_questions()
    guesses = []
    answers = []
    score = 0
    question_num = 0

    if not questions:
        print("Sorry, we couldn't load any quiz questions. Please try again.")
        return

    for question in questions:
        print("----------------------")
        print(f"Q{question_num + 1}: {question['question']}")

        options = question["options"]
        lettered_options = {
            "A": options[0],
            "B": options[1],
            "C": options[2],
            "D": options[3]
        }
        for letter, option in lettered_options.items():
            print(f"{letter}: {option}")
        while True:
            guess = input("Enter (A, B, C, D): ").upper()
            if validate_answer(guess, options):
                break
            else:
                print("Invalid input. Please choose A, B, C, or D.")
        clear_screen()

        guesses.append(guess)

        for letter, answer_text in lettered_options.items():
            if answer_text == question["correct"]:
                correct_letter = letter
                break

        answers.append(correct_letter)

        if guess == correct_letter:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_letter}.")
        question_num += 1
        time.sleep(1)

    show_final_results(answers, guesses, score)