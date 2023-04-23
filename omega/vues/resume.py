import tkinter as tk
from tkinter import ttk
from .. import controleur

def create_frame(parent):
    resume = tk.Frame(parent, bg="#800040")
    combo_value=["par Age","par sexe","par Shirt","par Pointure","par Statut"]
    combo_choice=ttk.Combobox(resume,values=combo_value)
    combo_choice.pack(ipady=1.5)

    recapitulatif=tk.Frame(resume,bg="#800040")
    recapitulatif.pack(side="left", fill="both", expand=True)

    trier=tk.Button(resume,text="TRIER",command=lambda:controleur.resumer(combo_choice.get(),recapitulatif),height=1)
    trier.place(relx=0.58,rely=0)
    
    return resume