import os


def validate_answer(user_input, options):
    """
    Validate user input.
    """
    valid_inputs = ['A', 'B', 'C', 'D']
    return user_input in valid_inputs and len(options) == 4


def clear_screen():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def show_final_results(answers, guesses, score):
    """
    Displays the final results and score summary.
    """
    print("\n----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("Answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    percentage = int(score / len(answers) * 100)
    print(f"\nYour score is: {percentage}%")

    if percentage == 100:
        print("You're a mythological master!")
    elif percentage >= 70:
        print("Great job! You know your myths.")
    elif percentage >= 50:
        print("Not bad! Brush up on your lore.")
    else:
        print("The gods are disappointed... try again!")
