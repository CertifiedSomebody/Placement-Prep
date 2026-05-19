import customtkinter as ctk

from logic.quiz_manager import QuizManager
from ui.home_screen import HomeScreen


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
# Quiz Manager
# =========================================
quiz = QuizManager()


# =========================================
# Temporary Function
# =========================================
def start_category(category_name):

    quiz.load_category(category_name)

    print(f"Selected Category: {category_name}")


# =========================================
# Home Screen
# =========================================
home_screen = HomeScreen(
    app,
    start_category
)


# =========================================
# Run App
# =========================================
app.mainloop()