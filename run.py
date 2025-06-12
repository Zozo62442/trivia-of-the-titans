import time
from game import start_quiz


def show_intro():
    print("""
    ▗▖  ▗▖▄   ▄    ■  ▐▌    ▄▄▄  █  ▄▄▄   ▄   ▄
    ▐▛▚▞▜▌█   █ ▗▄▟▙▄▖▐▌   █   █ █ █   █  █   █
    ▐▌  ▐▌ ▀▀▀█   ▐▌  ▐▛▀▚▖▀▄▄▄▀ █ ▀▄▄▄▀   ▀▀▀█
    ▐▌  ▐▌▄   █   ▐▌  ▐▌ ▐▌      █     ▗▄▖▄   █
           ▀▀▀    ▐▌                  ▐▌ ▐▌▀▀▀
                                       ▝▀▜▌
                                      ▐▙▄▞▘
   """)
    print("⚡ Welcome to *Trivia of the Titans* – The Ultimate Mythology Trivia Quiz! ⚡\n")
    print("Test your knowledge across 10 randomly selected mythology questions.")
    print("You’ll be asked multiple-choice questions from a vast ancient world.")
    print("Topics include Greek, Norse, Egyptian, and more!\n")
    print("Just type the letter of your chosen answer and hit Enter.\n")
    print("Let the challenge begin, hero! ✨\n")

while True:
    username = input("Please enter your adventurer name: ").strip()
    if username.isalnum():
        username = username.capitalize()
        break
    else:
        print("Invalid name! Please use only letters or letters and numbers (no symbols or spaces).")
    
    input("Press Enter to begin your quest... ")
    print("\nSummoning the gods...\n")
    time.sleep(1)
    return username


def main():
    show_intro()
    start_quiz(username)

if __name__ == "__main__":
    main()
