import customtkinter as ctk


class HistoryScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        db_manager,
        back_callback
    ):

        super().__init__(master)

        self.db = db_manager

        title_label = ctk.CTkLabel(
            self,
            text="Quiz History",
            font=("Arial", 36, "bold")
        )

        title_label.pack(pady=30)

        # =========================================
        # History Textbox
        # =========================================
        self.history_box = ctk.CTkTextbox(
            self,
            width=700,
            height=350,
            font=("Arial", 16)
        )

        self.history_box.pack(pady=20)

        # =========================================
        # Back Button
        # =========================================
        back_button = ctk.CTkButton(
            self,
            text="Back",
            width=200,
            height=50,
            font=("Arial", 18, "bold"),
            command=back_callback
        )

        back_button.pack(pady=20)

    # =========================================
    # Load History
    # =========================================
    def load_history(self):

        self.history_box.delete(
            "1.0",
            "end"
        )

        history = self.db.get_history()

        if not history:

            self.history_box.insert(
                "end",
                "No quiz history found."
            )

            return

        for item in history:

            category, score, total, played_at = item

            history_text = (
                f"Category: {category}\n"
                f"Score: {score}/{total}\n"
                f"Played At: {played_at}\n"
                f"{'-'*40}\n"
            )

            self.history_box.insert(
                "end",
                history_text
            )