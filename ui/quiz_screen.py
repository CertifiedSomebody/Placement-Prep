import customtkinter as ctk

from logic.timer_manager import TimerManager


class QuizScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        app,
        quiz_manager,
        show_result_callback
    ):

        super().__init__(master)

        self.quiz = quiz_manager
        self.show_result_callback = show_result_callback

        # =========================================
        # Timer Manager
        # =========================================
        self.timer = TimerManager(
            app,
            self.update_timer_label,
            self.handle_timeout
        )

        # =========================================
        # Progress Label
        # =========================================
        self.progress_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 18)
        )

        self.progress_label.pack(
            pady=(20, 5)
        )

        # =========================================
        # Timer Label
        # =========================================
        self.timer_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 18, "bold"),
            text_color="orange"
        )

        self.timer_label.pack(
            pady=(0, 20)
        )

        # =========================================
        # Question Label
        # =========================================
        self.question_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 26),
            wraplength=700
        )

        self.question_label.pack(
            pady=50
        )

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

        self.progress_label.configure(
            text=f"Question {self.quiz.current_question + 1} / {self.quiz.total_questions()}"
        )

        self.question_label.configure(
            text=question_data["question"]
        )

        for i, option in enumerate(question_data["options"]):

            self.option_buttons[i].configure(
                text=option
            )

        self.timer.start_timer()

    # =========================================
    # Check Answer
    # =========================================
    def check_answer(self, selected_option):

        self.timer.stop_timer()

        self.quiz.check_answer(selected_option)

        if self.quiz.has_questions_left():

            self.load_question()

        else:

            self.show_result_callback()

    # =========================================
    # Update Timer Label
    # =========================================
    def update_timer_label(self, time_left):

        self.timer_label.configure(
            text=f"Time Left: {time_left}s"
        )

    # =========================================
    # Handle Timeout
    # =========================================
    def handle_timeout(self):

        self.check_answer("")