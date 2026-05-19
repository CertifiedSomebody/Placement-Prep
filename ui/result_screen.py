import customtkinter as ctk


class ResultScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        quiz_manager,
        restart_callback
    ):

        super().__init__(master)

        self.quiz = quiz_manager
        self.restart_callback = restart_callback

        completed_label = ctk.CTkLabel(
            self,
            text="Quiz Completed!",
            font=("Arial", 36, "bold")
        )

        completed_label.pack(pady=50)

        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 28)
        )

        self.result_label.pack(pady=20)

        restart_button = ctk.CTkButton(
            self,
            text="Restart Quiz",
            width=220,
            height=55,
            font=("Arial", 20, "bold"),
            command=self.restart_callback
        )

        restart_button.pack(pady=40)

    # =========================================
    # Update Score
    # =========================================
    def update_score(self):

        self.result_label.configure(
            text=f"Your Score: {self.quiz.get_score()}/{self.quiz.total_questions()}"
        )