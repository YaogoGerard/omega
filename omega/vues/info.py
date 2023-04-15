import tkinter as tk

def create_frame(parent):
    info =tk.Frame(parent, bg="black")
    label = tk.Label(info, text="je suis la page info")
    label.pack(padx=10, pady=10)
    return info