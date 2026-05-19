import customtkinter as ctk


class QuizScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        quiz_manager,
        show_result_callback
    ):

        super().__init__(master)

        self.quiz = quiz_manager
        self.show_result_callback = show_result_callback

        # =========================================
        # Question Label
        # =========================================
        self.question_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 26),
            wraplength=700
        )

        self.question_label.pack(pady=50)

        # =========================================
        # Option Buttons
        # =========================================
        self.option_buttons = []

        for i in range(4):

            button = ctk.CTkButton(
                self,
                text="",
                width=450,
                height=55,
                font=("Arial", 18),
                command=lambda i=i: self.check_answer(
                    self.option_buttons[i].cget("text")
                )
            )

            button.pack(pady=12)

            self.option_buttons.append(button)

    # =========================================
    # Load Question
    # =========================================
    def load_question(self):

        question_data = self.quiz.get_question()

        self.question_label.configure(
            text=question_data["question"]
        )

        for i, option in enumerate(question_data["options"]):

            self.option_buttons[i].configure(
                text=option
            )

    # =========================================
    # Check Answer
    # =========================================
    def check_answer(self, selected_option):

        self.quiz.check_answer(selected_option)

        if self.quiz.has_questions_left():

            self.load_question()

        else:

            self.show_result_callback()