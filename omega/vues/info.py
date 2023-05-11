import tkinter as tk

def create_frame(parent):
    info =tk.Frame(parent, bg="#800040")
    label = tk.Message(info,width=500, text="Ce logiciel est destion destiné au Centre de Develeppement pour Enfants(CDE), il a été realiser par YAOGO Gérard Windpagnangdé du CDE BF-780.\n ceci est la première version du logiciel: la version 1, ce logiciel ne doit etre vendu en aucun cas , il a été developper pour faciliter le travail pour les responsables et agents de COMPASSION INTERNNAL.")
    label.pack(padx=10,pady=200)
    return info