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

    # scrolabilité
    def make_scrollable(treeview):
        # Création des scrollbars
        scrollbar_y = ttk.Scrollbar(rechercher, orient="vertical", command=treeview.yview)
        scrollbar_x = ttk.Scrollbar(rechercher, orient="horizontal", command=treeview.xview)

        # Configuration des scrollbars pour le treeview
        treeview.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Placement des scrollbars dans le treeview
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")


    # Gestion d'affichage
    
    affichage=tk.Frame(rechercher)
   
    affichage.pack(side="left",expand="true",fill="both")

    # Gestion du treeview
    resultats = ttk.Treeview(rechercher)
    make_scrollable(resultats)
    resultats.pack(side="right",expand="true",fill="both")
    resultats.heading('#0',text="Nom et Prenom")
    
    resultats.bind('<ButtonRelease-1>',lambda event:controleur.afficher(resultats,affichage))
    
    controleur.remplir_treeview(resultats)
    return rechercher