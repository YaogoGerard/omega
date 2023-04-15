import tkinter as tk
import tkinter.ttk as ttk

def create_frame(parent):
    rechercher = tk.Frame(parent, bg="#800040")
    barre=tk.Frame(rechercher,bg="#800040")
    barre.pack(pady="20")
    b1=tk.Button(barre,text="RECHERCHER")
    b1.grid(column=0,row=0)
    space=tk.Label(barre,width=5, bg="#800040")
    space.grid(column=1,row=0)
    champs=tk.Entry(barre,justify="center",width=80,relief="sunken")
    champs.grid(column=2,row=0)

    affichage=tk.Frame(rechercher)
    affichage.pack(side="left",expand="true",fill="both")
    resultats = ttk.Treeview(rechercher)
    resultats.pack(side="right",expand="true",fill="both")
    return rechercher