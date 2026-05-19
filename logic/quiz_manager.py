from data.questions import questions


class QuizManager:

    def __init__(self):

        self.questions = []
        self.current_question = 0
        self.score = 0

    def load_category(self, category_name):

        self.questions = questions[category_name]

        self.current_question = 0
        self.score = 0

    def get_question(self):

        return self.questions[self.current_question]

    def check_answer(self, selected_option):

        correct_answer = self.questions[self.current_question]["answer"]

        if selected_option == correct_answer:
            self.score += 1

        self.current_question += 1

    def has_questions_left(self):

        return self.current_question < len(self.questions)

    def get_score(self):

        return self.score

    def total_questions(self):

        return len(self.questions)

    def restart_quiz(self):

        self.current_question = 0
        self.score = 0