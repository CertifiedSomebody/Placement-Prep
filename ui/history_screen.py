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

        # =========================================
        # Title
        # =========================================
        title_label = ctk.CTkLabel(
            self,
            text="Quiz History",
            font=("Arial", 38, "bold")
        )

        title_label.pack(
            pady=(30, 10)
        )

        # =========================================
        # Subtitle
        # =========================================
        subtitle_label = ctk.CTkLabel(
            self,
            text="Track your previous quiz performances",
            font=("Arial", 18),
            text_color="gray"
        )

        subtitle_label.pack(
            pady=(0, 20)
        )

        # =========================================
        # Scrollable Frame
        # =========================================
        self.history_frame = ctk.CTkScrollableFrame(
            self,
            width=850,
            height=420,
            corner_radius=15
        )

        self.history_frame.pack(
            pady=20
        )

        # =========================================
        # Back Button
        # =========================================
        back_button = ctk.CTkButton(
            self,
            text="Back",
            width=220,
            height=50,
            font=("Arial", 18, "bold"),
            command=back_callback
        )

        back_button.pack(
            pady=20
        )

    # =========================================
    # Load History
    # =========================================
    def load_history(self):

        for widget in self.history_frame.winfo_children():

            widget.destroy()

        history = self.db.get_history()

        if not history:

            empty_label = ctk.CTkLabel(
                self.history_frame,
                text="No quiz history found.",
                font=("Arial", 20)
            )

            empty_label.pack(pady=30)

            return

        for item in history:

            category, score, total, percentage, played_at = item

            # =========================================
            # SAFE FIX (CRITICAL)
            # =========================================
            if percentage is None:

                if total and total > 0:

                    percentage = round((score / total) * 100, 2)

                else:

                    percentage = 0

            # Final safety
            percentage = float(percentage)

            # =========================================
            # Color Logic
            # =========================================
            if percentage >= 80:

                score_color = "lightgreen"

            elif percentage >= 60:

                score_color = "orange"

            else:

                score_color = "red"

            # =========================================
            # Card UI
            # =========================================
            card = ctk.CTkFrame(
                self.history_frame,
                corner_radius=15
            )

            card.pack(
                fill="x",
                padx=15,
                pady=10
            )

            category_label = ctk.CTkLabel(
                card,
                text=f"📘 {category}",
                font=("Arial", 24, "bold")
            )

            category_label.pack(
                anchor="w",
                padx=20,
                pady=(15, 5)
            )

            score_label = ctk.CTkLabel(
                card,
                text=f"Score: {score}/{total} ({percentage}%)",
                font=("Arial", 18, "bold"),
                text_color=score_color
            )

            score_label.pack(
                anchor="w",
                padx=20,
                pady=5
            )

            date_label = ctk.CTkLabel(
                card,
                text=f"Played At: {played_at}",
                font=("Arial", 16),
                text_color="gray"
            )

            date_label.pack(
                anchor="w",
                padx=20,
                pady=(5, 15)
            )