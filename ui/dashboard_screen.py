import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt


class DashboardScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        db_manager
    ):

        super().__init__(master)

        self.db = db_manager

        # =========================================
        # Title
        # =========================================
        title_label = ctk.CTkLabel(
            self,
            text="Analytics Dashboard",
            font=("Arial", 38, "bold")
        )

        title_label.pack(
            pady=(20, 10)
        )

        # =========================================
        # Subtitle
        # =========================================
        subtitle_label = ctk.CTkLabel(
            self,
            text="Track your placement preparation progress",
            font=("Arial", 18),
            text_color="gray"
        )

        subtitle_label.pack(
            pady=(0, 20)
        )

        # =========================================
        # Stats Frame
        # =========================================
        self.stats_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.stats_frame.pack(
            pady=10
        )

        # =========================================
        # Total Quizzes Card
        # =========================================
        self.total_card = ctk.CTkFrame(
            self.stats_frame,
            width=250,
            height=120,
            corner_radius=20
        )

        self.total_card.grid(
            row=0,
            column=0,
            padx=20
        )

        self.total_card.grid_propagate(False)

        total_title = ctk.CTkLabel(
            self.total_card,
            text="Total Quizzes",
            font=("Arial", 20, "bold")
        )

        total_title.pack(
            pady=(20, 5)
        )

        self.total_label = ctk.CTkLabel(
            self.total_card,
            text="0",
            font=("Arial", 34, "bold"),
            text_color="lightgreen"
        )

        self.total_label.pack()

        # =========================================
        # Average Score Card
        # =========================================
        self.average_card = ctk.CTkFrame(
            self.stats_frame,
            width=250,
            height=120,
            corner_radius=20
        )

        self.average_card.grid(
            row=0,
            column=1,
            padx=20
        )

        self.average_card.grid_propagate(False)

        average_title = ctk.CTkLabel(
            self.average_card,
            text="Average Score",
            font=("Arial", 20, "bold")
        )

        average_title.pack(
            pady=(20, 5)
        )

        self.average_label = ctk.CTkLabel(
            self.average_card,
            text="0%",
            font=("Arial", 34, "bold"),
            text_color="orange"
        )

        self.average_label.pack()

        # =========================================
        # Best Category Card
        # =========================================
        self.best_card = ctk.CTkFrame(
            self.stats_frame,
            width=250,
            height=120,
            corner_radius=20
        )

        self.best_card.grid(
            row=0,
            column=2,
            padx=20
        )

        self.best_card.grid_propagate(False)

        best_title = ctk.CTkLabel(
            self.best_card,
            text="Best Category",
            font=("Arial", 20, "bold")
        )

        best_title.pack(
            pady=(20, 5)
        )

        self.best_label = ctk.CTkLabel(
            self.best_card,
            text="-",
            font=("Arial", 26, "bold"),
            text_color="skyblue"
        )

        self.best_label.pack()

        # =========================================
        # Graph Frame
        # =========================================
        self.graph_frame = ctk.CTkFrame(
            self,
            corner_radius=20
        )

        self.graph_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=30
        )

    # =========================================
    # Load Dashboard Data
    # =========================================
    def load_dashboard(self):

        total_quizzes = self.db.get_total_quizzes()

        average_score = self.db.get_average_score()

        stats = self.db.get_category_stats()

        self.total_label.configure(
            text=str(total_quizzes)
        )

        self.average_label.configure(
            text=f"{average_score}%"
        )

        # =========================================
        # Best Category
        # =========================================
        if stats:

            best_category = max(
                stats,
                key=lambda item: item[1]
            )[0]

        else:

            best_category = "-"

        self.best_label.configure(
            text=best_category
        )

        self.load_graph()

    # =========================================
    # Load Graph
    # =========================================
    def load_graph(self):

        for widget in self.graph_frame.winfo_children():

            widget.destroy()

        stats = self.db.get_category_stats()

        if not stats:

            empty_label = ctk.CTkLabel(
                self.graph_frame,
                text="No analytics data available yet.",
                font=("Arial", 22)
            )

            empty_label.pack(
                pady=50
            )

            return

        categories = [item[0] for item in stats]

        counts = [item[1] for item in stats]

        # =========================================
        # Matplotlib Figure
        # =========================================
        fig, ax = plt.subplots(
            figsize=(7, 4)
        )

        fig.patch.set_facecolor("#2b2b2b")

        ax.set_facecolor("#2b2b2b")

        ax.bar(
            categories,
            counts
        )

        ax.set_title(
            "Quiz Attempts Per Category",
            color="white",
            fontsize=16
        )

        ax.set_xlabel(
            "Category",
            color="white"
        )

        ax.set_ylabel(
            "Attempts",
            color="white"
        )

        ax.tick_params(
            axis="x",
            colors="white"
        )

        ax.tick_params(
            axis="y",
            colors="white"
        )

        # =========================================
        # Embed Graph
        # =========================================
        canvas = FigureCanvasTkAgg(
            fig,
            master=self.graph_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )