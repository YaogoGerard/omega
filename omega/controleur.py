
import tkinter as tk
from tkinter import messagebox
from . import modele 
individu=modele.database()
def ajouter_element(nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel):
    if len(nom)==0 or len(prenom)==0 or len(age)==0 or len(classe)==0 or len(sexe)==0 or len(matricule)==0 or len(statut)==0:
        root=tk.Tk()
        root.withdraw()
        messagebox.showinfo("info","veuillez remplir tout les champs")
    else:
        individu.ajouter(nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel)
        nom.set()==""    
        prenom.set()=="" 
        age.set()==""
        classe.set()==""  
        matricule.set()=="" 
        shirt.set()==""

