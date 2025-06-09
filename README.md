# Trivia of the Titans

**Trivia of the Titans** is a command-line Python quiz game that tests your knowledge of mythology using randomly generated questions from the Open Trivia Database. The player answers 10 mythological questions and gets their final score at the end. 

[Live version of the project – hosted on Heroku]()

---

## How to Play

- Launch the app in the terminal.
- Choose to begin the mythological quiz.
- You’ll be asked **10 random mythology-themed questions**.
- For each question, select the correct answer from multiple choices.
- At the end, your score will be revealed!

Questions are pulled dynamically from [OpenTDB](https://opentdb.com), making each game different!

---

## Features

### Existing Features

- 10 randomised mythology questions per game
- Multiple choice answers
- Input validation: accepts only A/B/C/D (case-insensitive)
- Error messages for invalid input
- Final score presented at the end
- Live API integration (OpenTDB)
- Clean modular codebase (separated into `run.py`, `game.py`, `api.py`, `utile.py`)
- Fun, friendly terminal interface

### Future Features

- Category or difficulty selection
- Scoreboard or high score tracking
- Timed answers or “streak” bonuses
- Save stats to file or database
- More myth themes (Norse, Egyptian, etc.)

---

## Data Model

- Uses the **Open Trivia Database API** to fetch quiz questions.
- Each API response includes:
  - `question` (text)
  - `correct_answer`
  - `incorrect_answers` (list)
- These are combined and shuffled before being shown to the user.

---

## Testing

### Manual Tests


### Linter

- [PEP8 Online](https://pep8ci.herokuapp.com/).

---

## Bugs

### Solved Bugs



### Remaining Bugs

- None known at this time.

---

## 🚀 Deployment

This project is deployed using Code Institute’s mock terminal for Heroku or hosted on Replit.

### Deployment Steps:

1. Fork or clone this repository.
2. Create a new Heroku app or Replit project.
3. Set buildpacks: Python (and NodeJS for Heroku CLI if needed).
4. Add required dependencies in `requirements.txt`.
5. Add a `Procfile` containing:  

## Resources:
- ASCII generator [patorjk](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
- Youtube video [Bro Code](https://www.youtube.com/watch?v=zehwgTB0vV8)