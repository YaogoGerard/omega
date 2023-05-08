
import tkinter as tk
from tkinter import messagebox
from . import modele 
individu=modele.database()
def ajouter_element(nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel,a,b,c,d,e,f,g,h,i,j,k,l):
    
    if not nom :
        #or prenom.get() or age.get() or classe.get() or sexe.get() or matricule.get() or statut.get() or shirt.get() or pointure.get() or tel.get()
        root=tk.Tk()
        root.withdraw()
        messagebox.showinfo("info","veuillez remplir tout les champs")
        print(nom)
        root.destroy()
    else:
        individu.ajouter(nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel)
        messagebox.showinfo("info","Enregistrement reussit!")
        a.delete(0,tk.END)
        b.delete(0,tk.END)
        c.delete(0,tk.END)
        d.delete(0,tk.END)
        e.deselect()
        f.deselect()
        g.delete(0,tk.END)
        h.deselect()
        i.deselect()
        j.delete(0,tk.END)
        k.delete(0,tk.END)
        l.delete(0,tk.END)
        
        
        

       

def resumer(type,frame):

    individu.resume(type,frame)
