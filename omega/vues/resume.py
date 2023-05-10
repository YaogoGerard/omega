import tkinter as tk
from tkinter import ttk
from .. import controleur

def create_frame(parent):
    resume = tk.Frame(parent, bg="#800040")
    
    combo_value=["par Age","par sexe","par Shirt","par Pointure","par Statut"]
    combo_choice=ttk.Combobox(resume,values=combo_value)
    combo_choice.pack(padx=1.5)

    trier=tk.Button(resume,text="TRIER",command=lambda:controleur.resumer(combo_choice.get(),recapitulatif),height=1)
    trier.pack(padx=1.7)

    recapitulatif=tk.Frame(resume)
    recapitulatif.pack(ipadx=400,ipady=300,padx=15,fill="y",expand=True)

    
    
    return resume