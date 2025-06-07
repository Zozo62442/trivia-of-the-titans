from api import get_questions
from utils import validate_answer, show_final_results
import time

def start_quiz(username):
    """
    Runs the main quiz game loop.
    """
    clear_screen()
    print(f"🎉 Welcome to Trivia of Titans {username}! \n")
    print("You'll be asked 10 mythology questions. Choose the correct answer by typing A, B, C, or D (it is case sensitive)!\n")
    time.sleep(2)
    # 1. Fetch questions
    questions = get_questions()
    guesses = []
    answers = []
    score = 0
    question_num = 0

    if not questions:
        print("❌ Sorry, we couldn't load any quiz questions. Please try later.")
        return

    # 2. Loop through them
    for q in questions:
        print("----------------------")
        print(f"Q{question_num + 1}: {q['question']}")

    # 3. Display each question and choices
    # 4. Get user input and check if it's correct
    # 5. Track score
    # 6. Show final result

