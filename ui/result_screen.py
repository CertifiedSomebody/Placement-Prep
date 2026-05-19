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

        # =========================================
        # Title
        # =========================================
        completed_label = ctk.CTkLabel(
            self,
            text="Quiz Completed!",
            font=("Arial", 38, "bold")
        )

        completed_label.pack(
            pady=(50, 20)
        )

        # =========================================
        # Score Label
        # =========================================
        self.result_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 30, "bold")
        )

        self.result_label.pack(
            pady=10
        )

        # =========================================
        # Percentage Label
        # =========================================
        self.percentage_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 24)
        )

        self.percentage_label.pack(
            pady=10
        )

        # =========================================
        # Performance Label
        # =========================================
        self.performance_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 24, "bold")
        )

        self.performance_label.pack(
            pady=20
        )

        # =========================================
        # Restart Button
        # =========================================
        restart_button = ctk.CTkButton(
            self,
            text="Restart Quiz",
            width=240,
            height=55,
            font=("Arial", 20, "bold"),
            command=self.restart_callback
        )

        restart_button.pack(
            pady=40
        )

    # =========================================
    # Update Score
    # =========================================
    def update_score(self):

        score = self.quiz.get_score()

        total = self.quiz.total_questions()

        percentage = round(
            (score / total) * 100,
            2
        )

        self.result_label.configure(
            text=f"Your Score: {score}/{total}"
        )

        self.percentage_label.configure(
            text=f"Percentage: {percentage}%"
        )

        # =========================================
        # Performance Feedback
        # =========================================
        if percentage >= 80:

            performance_text = "Excellent Performance! 🔥"

            color = "lightgreen"

        elif percentage >= 60:

            performance_text = "Good Job! 👍"

            color = "orange"

        else:

            performance_text = "Keep Practicing! 📚"

            color = "red"

        self.performance_label.configure(
            text=performance_text,
            text_color=color
        )