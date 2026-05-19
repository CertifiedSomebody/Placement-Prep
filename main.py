import customtkinter as ctk

from logic.quiz_manager import QuizManager
from database.db_manager import DatabaseManager

from ui.sidebar import Sidebar
from ui.home_screen import HomeScreen
from ui.quiz_screen import QuizScreen
from ui.result_screen import ResultScreen
from ui.history_screen import HistoryScreen
from ui.dashboard_screen import DashboardScreen


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
# Main Content Area
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
# Utility Functions
# =========================================
def clear_screens():

    for widget in content_frame.winfo_children():

        widget.pack_forget()


def show_screen(screen):

    clear_screens()

    screen.pack(
        fill="both",
        expand=True
    )


# =========================================
# Navigation Functions
# =========================================
def show_home():

    show_screen(home_screen)


def show_dashboard():

    dashboard_screen.load_dashboard()

    show_screen(dashboard_screen)


def open_history():

    history_screen.load_history()

    show_screen(history_screen)


# =========================================
# Quiz Flow
# =========================================
def start_category(category_name):

    quiz.load_category(category_name)

    show_screen(quiz_screen)

    quiz_screen.load_question()


def show_result():

    db.save_result(
        quiz.current_category,
        quiz.get_score(),
        quiz.total_questions()
    )

    result_screen.update_score()

    show_screen(result_screen)


def restart_quiz():

    quiz.restart_quiz()

    show_home()


# =========================================
# Safe Exit
# =========================================
def close_app():

    try:

        if hasattr(quiz_screen, "timer"):

            quiz_screen.timer.stop_timer()

    except Exception:

        pass

    try:

        db.connection.close()

    except Exception:

        pass

    app.quit()

    app.destroy()


# =========================================
# Sidebar
# =========================================
sidebar = Sidebar(
    app,
    show_home,
    show_dashboard,
    open_history,
    close_app
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

dashboard_screen = DashboardScreen(
    content_frame,
    db
)


# =========================================
# Window Close Protocol
# =========================================
app.protocol(
    "WM_DELETE_WINDOW",
    close_app
)


# =========================================
# Default Screen
# =========================================
show_home()


# =========================================
# Run Application
# =========================================
app.mainloop()