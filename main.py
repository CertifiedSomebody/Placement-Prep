import customtkinter as ctk


# -----------------------------
# App Configuration
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# -----------------------------
# Main App Window
# -----------------------------
app = ctk.CTk()

app.title("PlacementPrep")
app.geometry("900x600")
app.resizable(False, False)


# -----------------------------
# Title Label
# -----------------------------
title_label = ctk.CTkLabel(
    app,
    text="PlacementPrep",
    font=("Arial", 36, "bold")
)

title_label.pack(pady=50)


# -----------------------------
# Subtitle
# -----------------------------
subtitle_label = ctk.CTkLabel(
    app,
    text="Train for Placements Efficiently",
    font=("Arial", 18)
)

subtitle_label.pack(pady=10)


# -----------------------------
# Start Quiz Button
# -----------------------------
start_button = ctk.CTkButton(
    app,
    text="Start Quiz",
    width=200,
    height=50,
    font=("Arial", 18, "bold")
)

start_button.pack(pady=40)


# -----------------------------
# Run App
# -----------------------------
app.mainloop()