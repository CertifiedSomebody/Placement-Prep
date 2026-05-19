import customtkinter as ctk


class HomeScreen(ctk.CTkFrame):

    def __init__(self, master, start_category_callback):

        super().__init__(master)

        self.pack(
            fill="both",
            expand=True
        )

        title_label = ctk.CTkLabel(
            self,
            text="PlacementPrep",
            font=("Arial", 40, "bold")
        )

        title_label.pack(pady=50)

        subtitle_label = ctk.CTkLabel(
            self,
            text="Choose a Quiz Category",
            font=("Arial", 20)
        )

        subtitle_label.pack(pady=10)

        aptitude_button = ctk.CTkButton(
            self,
            text="Aptitude",
            width=250,
            height=55,
            font=("Arial", 18, "bold"),
            command=lambda: start_category_callback("Aptitude")
        )

        aptitude_button.pack(pady=15)

        programming_button = ctk.CTkButton(
            self,
            text="Programming",
            width=250,
            height=55,
            font=("Arial", 18, "bold"),
            command=lambda: start_category_callback("Programming")
        )

        programming_button.pack(pady=15)

        logical_button = ctk.CTkButton(
            self,
            text="Logical Reasoning",
            width=250,
            height=55,
            font=("Arial", 18, "bold"),
            command=lambda: start_category_callback("Logical Reasoning")
        )

        logical_button.pack(pady=15)