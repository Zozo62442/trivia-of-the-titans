import requests
import random

def get_questions():
    """
    Fetches 10 multiple choice questions from the OpenTDB API
    and returns them.
    """
    url = "https://opentdb.com/api.php?amount=10&category=20&type=multiple"
    response = requests.get(url)
    data = response.json()

    questions = []

    for item in data["results"]:
        question = item["question"]
        correct = item["correct_answer"]
        incorrect = [ans for ans in item["incorrect_answers"]]
        options = incorrect + [correct]

        random.shuffle(options)

        questions.append({
            "question": question,
            "options": options,
            "correct": correct
        })

    return questions