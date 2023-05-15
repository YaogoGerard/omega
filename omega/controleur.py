
import tkinter as tk
from tkinter import messagebox
from . import modele 
individu=modele.database()

def afficher(resultats,conteneur):
    for widget in conteneur.winfo_children():
        widget.destroy()
    individu.afficher(resultats,conteneur)

def rechercher(entree,treev):
    individu.rechercher(entree,treev)

def remplir_treeview(tree):
    individu.remplir_treeview(tree)

def ajouter_element(nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel,a,b,c,d,e,f,g,h,i,j,k,l):
    
    if not nom :
        #or not prenom or not age or not classe or not sexe or not matricule or not statut or not shirt or not pointure or not tel
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
    for widget in frame.winfo_children():
        widget.destroy()
    individu.resume(type,frame)
