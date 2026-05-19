from data.questions import questions


class QuizManager:

    def __init__(self):

        self.questions = []

        self.current_question = 0

        self.score = 0

        self.current_category = ""

    # =========================================
    # Load Category
    # =========================================
    def load_category(self, category_name):

        self.current_category = category_name

        self.questions = questions[category_name]

        self.current_question = 0

        self.score = 0

    # =========================================
    # Get Current Question
    # =========================================
    def get_question(self):

        return self.questions[self.current_question]

    # =========================================
    # Check Answer
    # =========================================
    def check_answer(self, selected_option):

        correct_answer = self.questions[self.current_question]["answer"]

        if selected_option == correct_answer:

            self.score += 1

        self.current_question += 1

    # =========================================
    # Questions Left
    # =========================================
    def has_questions_left(self):

        return self.current_question < len(self.questions)

    # =========================================
    # Get Score
    # =========================================
    def get_score(self):

        return self.score

    # =========================================
    # Total Questions
    # =========================================
    def total_questions(self):

        return len(self.questions)

    # =========================================
    # Restart Quiz
    # =========================================
    def restart_quiz(self):

        self.current_question = 0

        self.score = 0