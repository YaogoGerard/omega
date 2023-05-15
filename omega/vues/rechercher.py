import tkinter as tk
import tkinter.ttk as ttk
from .. import controleur

def create_frame(parent):
    rechercher = tk.Frame(parent, bg="#800040")
    barre=tk.Frame(rechercher,bg="#800040")
    barre.pack(pady="20")
    b1=tk.Button(barre,text="RECHERCHER",command=lambda:controleur.rechercher(champs,resultats))
    b1.grid(column=0,row=0)
    space=tk.Label(barre,width=5, bg="#800040")
    space.grid(column=1,row=0)
    # Gestion de l'entry

    champs=tk.Entry(barre,justify="center",width=80,relief="sunken")
    champs.grid(column=2,row=0)
    champs.bind('<KeyRelease>',lambda event:controleur.rechercher(champs.get(),resultats))

    # Gestion d'affichage
    conteneur_de_affichage=tk.Canvas(rechercher)
    conteneur_de_affichage.pack(side="left",expand="true",fill="both")

    yscrollbar=ttk.Scrollbar(conteneur_de_affichage,orient="vertical")
    yscrollbar.pack(side="right",fill="y")

    xscrollbar=ttk.Scrollbar(conteneur_de_affichage,orient="horizontal")
    xscrollbar.pack(side="bottom",fill="x")

    affichage=tk.Frame(conteneur_de_affichage)
    affichage.pack(side="left",expand="true",fill="both")

    # Gestion du treeview

    conteneur_de_resultats=tk.Canvas(rechercher)
    conteneur_de_resultats.pack(side="left",expand="true",fill="both")

    yscrollbar=ttk.Scrollbar(conteneur_de_resultats,orient="vertical")
    yscrollbar.pack(side="right",fill="y")

    xscrollbar=ttk.Scrollbar(conteneur_de_resultats,orient="horizontal")
    xscrollbar.pack(side="bottom",fill="x")

    resultats = ttk.Treeview(conteneur_de_resultats)
    resultats.pack(side="right",expand="true",fill="both")
    resultats.heading('#0',text="Nom et Prenom")
    
    resultats.bind('<ButtonRelease-1>',lambda event:controleur.afficher(resultats,affichage))
    
    controleur.remplir_treeview(resultats)
    return rechercher