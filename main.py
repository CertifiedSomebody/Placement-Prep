import customtkinter as ctk
from questions import questions


# -----------------------------
# App Setup
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x600")
app.title("PlacementPrep")


# -----------------------------
# Quiz Variables
# -----------------------------
current_question = 0
score = 0


# -----------------------------
# Functions
# -----------------------------
def load_question():

    question_data = questions[current_question]

    question_label.configure(
        text=question_data["question"]
    )

    for i, option in enumerate(question_data["options"]):
        option_buttons[i].configure(text=option)


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

    question_label.configure(
        text=f"Quiz Completed!\nYour Score: {score}/{len(questions)}"
    )

    for button in option_buttons:
        button.pack_forget()


# -----------------------------
# UI Elements
# -----------------------------
title_label = ctk.CTkLabel(
    app,
    text="PlacementPrep",
    font=("Arial", 32, "bold")
)

title_label.pack(pady=20)


question_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 24),
    wraplength=700
)

question_label.pack(pady=40)


option_buttons = []

for i in range(4):

    button = ctk.CTkButton(
        app,
        text="",
        width=400,
        height=50,
        font=("Arial", 18),
        command=lambda i=i: check_answer(
            option_buttons[i].cget("text")
        )
    )

    button.pack(pady=10)

    option_buttons.append(button)


# -----------------------------
# Start Quiz
# -----------------------------
load_question()


# -----------------------------
# Run App
# -----------------------------
app.mainloop()