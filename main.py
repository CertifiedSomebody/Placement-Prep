import customtkinter as ctk

from logic.quiz_manager import QuizManager

from database.db_manager import DatabaseManager

from ui.home_screen import HomeScreen
from ui.quiz_screen import QuizScreen
from ui.result_screen import ResultScreen
from ui.history_screen import HistoryScreen


# =========================================
# App Setup
# =========================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.geometry("900x600")
app.title("PlacementPrep")
app.resizable(False, False)


# =========================================
# Managers
# =========================================
quiz = QuizManager()

db = DatabaseManager()


# =========================================
# Functions
# =========================================
def start_category(category_name):

    quiz.load_category(category_name)

    home_screen.pack_forget()

    quiz_screen.pack(
        fill="both",
        expand=True
    )

    quiz_screen.load_question()


def show_result():

    quiz_screen.pack_forget()

    db.save_result(
        quiz.current_category,
        quiz.get_score(),
        quiz.total_questions()
    )

    result_screen.update_score()

    result_screen.pack(
        fill="both",
        expand=True
    )


def restart_quiz():

    quiz.restart_quiz()

    result_screen.pack_forget()

    home_screen.pack(
        fill="both",
        expand=True
    )


def open_history():

    home_screen.pack_forget()

    history_screen.load_history()

    history_screen.pack(
        fill="both",
        expand=True
    )


def close_history():

    history_screen.pack_forget()

    home_screen.pack(
        fill="both",
        expand=True
    )


# =========================================
# Screens
# =========================================
home_screen = HomeScreen(
    app,
    start_category,
    open_history
)

quiz_screen = QuizScreen(
    app,
    app,
    quiz,
    show_result
)

result_screen = ResultScreen(
    app,
    quiz,
    restart_quiz
)

history_screen = HistoryScreen(
    app,
    db,
    close_history
)


# =========================================
# Run App
# =========================================
app.mainloop()