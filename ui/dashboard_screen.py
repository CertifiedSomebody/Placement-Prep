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
            font=("Arial", 36, "bold")
        )

        title_label.pack(pady=20)

        # =========================================
        # Stats Labels
        # =========================================
        self.total_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 22)
        )

        self.total_label.pack(pady=10)

        self.average_label = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 22)
        )

        self.average_label.pack(pady=10)

        # =========================================
        # Graph Frame
        # =========================================
        self.graph_frame = ctk.CTkFrame(self)

        self.graph_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # =========================================
    # Load Dashboard Data
    # =========================================
    def load_dashboard(self):

        total_quizzes = self.db.get_total_quizzes()

        average_score = self.db.get_average_score()

        self.total_label.configure(
            text=f"Total Quizzes Played: {total_quizzes}"
        )

        self.average_label.configure(
            text=f"Average Score: {average_score}"
        )

        self.load_graph()

    # =========================================
    # Load Graph
    # =========================================
    def load_graph(self):

        for widget in self.graph_frame.winfo_children():

            widget.destroy()

        stats = self.db.get_category_stats()

        categories = [item[0] for item in stats]

        counts = [item[1] for item in stats]

        fig, ax = plt.subplots(figsize=(6, 4))

        ax.bar(categories, counts)

        ax.set_title("Quiz Attempts Per Category")

        ax.set_xlabel("Category")

        ax.set_ylabel("Attempts")

        canvas = FigureCanvasTkAgg(
            fig,
            master=self.graph_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )