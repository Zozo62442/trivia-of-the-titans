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

    username = input("Please enter your adventurer name: ").strip().capitalize()

    input("Press Enter to begin your quest... ")
    print("\nSummoning the gods...\n")
    time.sleep(1)

def main():
    show_intro()
    start_quiz()

if __name__ == "__main__":
    main()