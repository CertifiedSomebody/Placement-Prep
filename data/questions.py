import json


# =========================================
# Load Questions From JSON
# =========================================
def load_questions():

    with open(
        "data/questions/aptitude.json",
        "r"
    ) as file:

        aptitude_questions = json.load(file)

    with open(
        "data/questions/programming.json",
        "r"
    ) as file:

        programming_questions = json.load(file)

    with open(
        "data/questions/logical_reasoning.json",
        "r"
    ) as file:

        logical_questions = json.load(file)

    return {

        "Aptitude": aptitude_questions,

        "Programming": programming_questions,

        "Logical Reasoning": logical_questions
    }


questions = load_questions()