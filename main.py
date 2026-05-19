import customtkinter as ctk
from quiz_manager import QuizManager


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
# Functions
# =========================================
def start_quiz():

    home_frame.pack_forget()

    quiz_frame.pack(
        fill="both",
        expand=True
    )

    load_question()


def load_question():

    question_data = quiz.get_question()

    question_label.configure(
        text=question_data["question"]
    )

    for i, option in enumerate(question_data["options"]):

        option_buttons[i].configure(
            text=option
        )


def check_answer(selected_option):

    quiz.check_answer(selected_option)

    if quiz.has_questions_left():

        load_question()

    else:

        show_result()


def show_result():

    quiz_frame.pack_forget()

    result_label.configure(
        text=f"Your Score: {quiz.get_score()}/{quiz.total_questions()}"
    )

    result_frame.pack(
        fill="both",
        expand=True
    )


def restart_quiz():

    quiz.restart_quiz()

    result_frame.pack_forget()

    home_frame.pack(
        fill="both",
        expand=True
    )


# =========================================
# Home Frame
# =========================================
home_frame = ctk.CTkFrame(app)

title_label = ctk.CTkLabel(
    home_frame,
    text="PlacementPrep",
    font=("Arial", 40, "bold")
)

title_label.pack(pady=50)

subtitle_label = ctk.CTkLabel(
    home_frame,
    text="Choose a Quiz Category",
    font=("Arial", 20)
)

subtitle_label.pack(pady=10)


def start_category(category_name):

    quiz.load_category(category_name)

    start_quiz()


aptitude_button = ctk.CTkButton(
    home_frame,
    text="Aptitude",
    width=250,
    height=55,
    font=("Arial", 18, "bold"),
    command=lambda: start_category("Aptitude")
)

aptitude_button.pack(pady=15)


programming_button = ctk.CTkButton(
    home_frame,
    text="Programming",
    width=250,
    height=55,
    font=("Arial", 18, "bold"),
    command=lambda: start_category("Programming")
)

programming_button.pack(pady=15)


logical_button = ctk.CTkButton(
    home_frame,
    text="Logical Reasoning",
    width=250,
    height=55,
    font=("Arial", 18, "bold"),
    command=lambda: start_category("Logical Reasoning")
)

logical_button.pack(pady=15)


home_frame.pack(
    fill="both",
    expand=True
)

# =========================================
# Quiz Frame
# =========================================
quiz_frame = ctk.CTkFrame(app)

question_label = ctk.CTkLabel(
    quiz_frame,
    text="",
    font=("Arial", 26),
    wraplength=700
)

question_label.pack(pady=50)

option_buttons = []

for i in range(4):

    button = ctk.CTkButton(
        quiz_frame,
        text="",
        width=450,
        height=55,
        font=("Arial", 18),
        command=lambda i=i: check_answer(
            option_buttons[i].cget("text")
        )
    )

    button.pack(pady=12)

    option_buttons.append(button)


# =========================================
# Result Frame
# =========================================
result_frame = ctk.CTkFrame(app)

completed_label = ctk.CTkLabel(
    result_frame,
    text="Quiz Completed!",
    font=("Arial", 36, "bold")
)

completed_label.pack(pady=50)

result_label = ctk.CTkLabel(
    result_frame,
    text="",
    font=("Arial", 28)
)

result_label.pack(pady=20)

restart_button = ctk.CTkButton(
    result_frame,
    text="Restart Quiz",
    width=220,
    height=55,
    font=("Arial", 20, "bold"),
    command=restart_quiz
)

restart_button.pack(pady=40)


# =========================================
# Run App
# =========================================
app.mainloop()