
import tkinter as tk
from tkinter import messagebox
from . import modele 
individu=modele.database()
def ajouter_element(nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel):
    
    if nom.get()=="" :
        #or prenom.get() or age.get() or classe.get() or sexe.get() or matricule.get() or statut.get() or shirt.get() or pointure.get() or tel.get()
        root=tk.Tk()
        root.withdraw()
        messagebox.showinfo("info","veuillez remplir tout les champs")
        print(nom)
        root.destroy()
    else:
        individu.ajouter(nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel)
       

def resumer(type,frame):
    individu.resume(type,frame)
