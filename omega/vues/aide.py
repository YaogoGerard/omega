import tkinter as tk

def create_frame(parent):
    aide =tk.Frame(parent, bg="pink")
    label = tk.Label(aide, text="je suis la page aide")
    label.pack(padx=10, pady=10)
    return aide