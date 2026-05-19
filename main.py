import customtkinter as ctk
from questions import questions


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
# Quiz Variables
# =========================================
current_question = 0
score = 0


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

    question_data = questions[current_question]

    question_label.configure(
        text=question_data["question"]
    )

    for i, option in enumerate(question_data["options"]):
        option_buttons[i].configure(
            text=option
        )


def check_answer(selected_option):

    global current_question
    global score

    correct_answer = questions[current_question]["answer"]

    if selected_option == correct_answer:
        score += 1

    current_question += 1

    if current_question < len(questions):
        load_question()

    else:
        show_result()


def show_result():

    quiz_frame.pack_forget()

    result_label.configure(
        text=f"Your Score: {score}/{len(questions)}"
    )

    result_frame.pack(
        fill="both",
        expand=True
    )


def restart_quiz():

    global current_question
    global score

    current_question = 0
    score = 0

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

title_label.pack(pady=80)

subtitle_label = ctk.CTkLabel(
    home_frame,
    text="Train for Placements Efficiently",
    font=("Arial", 20)
)

subtitle_label.pack(pady=10)

start_button = ctk.CTkButton(
    home_frame,
    text="Start Quiz",
    width=220,
    height=55,
    font=("Arial", 20, "bold"),
    command=start_quiz
)

start_button.pack(pady=50)

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