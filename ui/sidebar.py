import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(
        self,
        master,
        home_callback,
        history_callback,
        exit_callback
    ):

        super().__init__(
            master,
            width=220,
            corner_radius=0
        )

        self.pack_propagate(False)

        # =========================================
        # App Title
        # =========================================
        title_label = ctk.CTkLabel(
            self,
            text="PlacementPrep",
            font=("Arial", 28, "bold")
        )

        title_label.pack(
            pady=(40, 50)
        )

        # =========================================
        # Home Button
        # =========================================
        home_button = ctk.CTkButton(
            self,
            text="Home",
            height=50,
            font=("Arial", 18),
            command=home_callback
        )

        home_button.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # =========================================
        # History Button
        # =========================================
        history_button = ctk.CTkButton(
            self,
            text="History",
            height=50,
            font=("Arial", 18),
            command=history_callback
        )

        history_button.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # =========================================
        # Exit Button
        # =========================================
        exit_button = ctk.CTkButton(
            self,
            text="Exit",
            height=50,
            font=("Arial", 18),
            fg_color="darkred",
            hover_color="#5c0000",
            command=exit_callback
        )

        exit_button.pack(
            fill="x",
            padx=20,
            pady=(350, 10)
        )