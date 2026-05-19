import customtkinter as ctk


class HomeScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        start_category_callback,
        open_history_callback
    ):

        super().__init__(master)

        self.pack(
            fill="both",
            expand=True
        )

        # =========================================
        # Title
        # =========================================
        title_label = ctk.CTkLabel(
            self,
            text="PlacementPrep",
            font=("Arial", 42, "bold")
        )

        title_label.pack(
            pady=(40, 10)
        )

        # =========================================
        # Subtitle
        # =========================================
        subtitle_label = ctk.CTkLabel(
            self,
            text="Sharpen Your Placement Skills",
            font=("Arial", 22),
            text_color="gray"
        )

        subtitle_label.pack(
            pady=(0, 40)
        )

        # =========================================
        # Categories Frame
        # =========================================
        categories_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        categories_frame.pack(
            pady=20
        )

        # =========================================
        # Aptitude Card
        # =========================================
        aptitude_frame = ctk.CTkFrame(
            categories_frame,
            width=250,
            height=180,
            corner_radius=20
        )

        aptitude_frame.grid(
            row=0,
            column=0,
            padx=20
        )

        aptitude_frame.grid_propagate(False)

        aptitude_title = ctk.CTkLabel(
            aptitude_frame,
            text="Aptitude",
            font=("Arial", 24, "bold")
        )

        aptitude_title.pack(
            pady=(25, 10)
        )

        aptitude_desc = ctk.CTkLabel(
            aptitude_frame,
            text="Practice percentages,\nprofit-loss,\nratios and more.",
            font=("Arial", 15),
            justify="center"
        )

        aptitude_desc.pack(
            pady=10
        )

        aptitude_button = ctk.CTkButton(
            aptitude_frame,
            text="Start",
            width=150,
            command=lambda: start_category_callback("Aptitude")
        )

        aptitude_button.pack(
            pady=15
        )

        # =========================================
        # Programming Card
        # =========================================
        programming_frame = ctk.CTkFrame(
            categories_frame,
            width=250,
            height=180,
            corner_radius=20
        )

        programming_frame.grid(
            row=0,
            column=1,
            padx=20
        )

        programming_frame.grid_propagate(False)

        programming_title = ctk.CTkLabel(
            programming_frame,
            text="Programming",
            font=("Arial", 24, "bold")
        )

        programming_title.pack(
            pady=(25, 10)
        )

        programming_desc = ctk.CTkLabel(
            programming_frame,
            text="Test coding,\nDSA and computer\nscience basics.",
            font=("Arial", 15),
            justify="center"
        )

        programming_desc.pack(
            pady=10
        )

        programming_button = ctk.CTkButton(
            programming_frame,
            text="Start",
            width=150,
            command=lambda: start_category_callback("Programming")
        )

        programming_button.pack(
            pady=15
        )

        # =========================================
        # Logical Reasoning Card
        # =========================================
        logical_frame = ctk.CTkFrame(
            categories_frame,
            width=250,
            height=180,
            corner_radius=20
        )

        logical_frame.grid(
            row=0,
            column=2,
            padx=20
        )

        logical_frame.grid_propagate(False)

        logical_title = ctk.CTkLabel(
            logical_frame,
            text="Logical",
            font=("Arial", 24, "bold")
        )

        logical_title.pack(
            pady=(25, 10)
        )

        logical_desc = ctk.CTkLabel(
            logical_frame,
            text="Improve logical\nthinking and\nreasoning skills.",
            font=("Arial", 15),
            justify="center"
        )

        logical_desc.pack(
            pady=10
        )

        logical_button = ctk.CTkButton(
            logical_frame,
            text="Start",
            width=150,
            command=lambda: start_category_callback("Logical Reasoning")
        )

        logical_button.pack(
            pady=15
        )

        # =========================================
        # Bottom Buttons
        # =========================================
        bottom_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        bottom_frame.pack(
            pady=40
        )

        history_button = ctk.CTkButton(
            bottom_frame,
            text="View History",
            width=220,
            height=50,
            font=("Arial", 18),
            command=open_history_callback
        )

        history_button.grid(
            row=0,
            column=0,
            padx=10
        )