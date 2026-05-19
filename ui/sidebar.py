import customtkinter as ctk
from tkinter import messagebox


class Sidebar(ctk.CTkFrame):
    def __init__(
        self,
        master,
        home_callback,
        dashboard_callback,
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
        # Exit Function
        # =========================================
        def confirm_exit():

            confirm = messagebox.askyesno(
                "Exit",
                "Are you sure you want to exit?"
            )

            if confirm:

                exit_callback()

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
        # Dashboard Button
        # =========================================
        dashboard_button = ctk.CTkButton(
            self,
            text="Dashboard",
            height=50,
            font=("Arial", 18),
            command=dashboard_callback
        )

        dashboard_button.pack(
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
            command=confirm_exit
        )

        exit_button.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=20
        )