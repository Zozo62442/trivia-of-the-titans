import requests
import html

def get_questions():
    """
    Fetches 10 multiple choice questions from the OpenTDB API
    and returns them.
    """
    url = "https://opentdb.com/api.php?amount=10&category=20&type=multiple"
    response = requests.get(url)
    data = response.json()

    questions = []
    