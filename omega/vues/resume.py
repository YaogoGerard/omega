import tkinter as tk
from tkinter import ttk
from .. import controleur

def create_frame(parent):
    resume = tk.Frame(parent, bg="#800040")
    combo_value=["par Age","par sexe","par Shirt","par Pointure","par Statut"]
    combo_choice=ttk.Combobox(resume,values=combo_value)
    combo_choice.pack()
    combo_selection=combo_choice.get()
    recapitulatif=tk.Frame(resume,bg="#800040")
    recapitulatif.pack(side="left", fill="both", expand=True)
    recapitulatif.config(takefocus=True)
    controleur.resumer(combo_selection,recapitulatif)
    return resume