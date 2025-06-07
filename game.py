from api import get_questions
from utils import get_user_choice, clear_screen
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
    # 2. Loop through them
    # 3. Display each question and choices
    # 4. Get user input and check if it's correct
    # 5. Track score
    # 6. Show final result

