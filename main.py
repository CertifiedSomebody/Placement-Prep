import customtkinter as ctk

from logic.quiz_manager import QuizManager

from database.db_manager import DatabaseManager

from ui.sidebar import Sidebar
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

app.geometry("1200x700")
app.title("PlacementPrep")

app.resizable(False, False)


# =========================================
# Managers
# =========================================
quiz = QuizManager()

db = DatabaseManager()


# =========================================
# Main Content Frame
# =========================================
content_frame = ctk.CTkFrame(
    app,
    corner_radius=0
)

content_frame.pack(
    side="right",
    fill="both",
    expand=True
)


# =========================================
# Screen Functions
# =========================================
def clear_screens():

    for widget in content_frame.winfo_children():

        widget.pack_forget()


def show_home():

    clear_screens()

    home_screen.pack(
        fill="both",
        expand=True
    )


def start_category(category_name):

    quiz.load_category(category_name)

    clear_screens()

    quiz_screen.pack(
        fill="both",
        expand=True
    )

    quiz_screen.load_question()


def show_result():

    db.save_result(
        quiz.current_category,
        quiz.get_score(),
        quiz.total_questions()
    )

    clear_screens()

    result_screen.update_score()

    result_screen.pack(
        fill="both",
        expand=True
    )


def restart_quiz():

    quiz.restart_quiz()

    show_home()


def open_history():

    clear_screens()

    history_screen.load_history()

    history_screen.pack(
        fill="both",
        expand=True
    )


# =========================================
# Sidebar
# =========================================
sidebar = Sidebar(
    app,
    show_home,
    open_history,
    app.destroy
)

sidebar.pack(
    side="left",
    fill="y"
)


# =========================================
# Screens
# =========================================
home_screen = HomeScreen(
    content_frame,
    start_category,
    open_history
)

quiz_screen = QuizScreen(
    content_frame,
    app,
    quiz,
    show_result
)

result_screen = ResultScreen(
    content_frame,
    quiz,
    restart_quiz
)

history_screen = HistoryScreen(
    content_frame,
    db,
    show_home
)


# =========================================
# Default Screen
# =========================================
show_home()


# =========================================
# Run App
# =========================================
app.mainloop()