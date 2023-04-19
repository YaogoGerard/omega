import tkinter as tk
import tkinter.ttk as ttk
from .. import controleur



def create_frame(parent):
    ajouter= tk.Frame(parent,bg="#800040")
    formulaire=tk.Frame(ajouter,bg="#808040",width=500,height=500)
    formulaire.pack(pady=60)

    element_nom=tk.StringVar()
    label_nom=tk.Label(formulaire,text="NOM",bg="#808040")
    label_nom.place(relx=0.1,rely=0.05)
    entry_nom=tk.Entry(formulaire,width=15,textvariable=element_nom)
    entry_nom.place(relx=0.18,rely=0.05)
    
    
   
    element_prenom=tk.StringVar()
    label_prenom=tk.Label(formulaire,text="PRENOM",bg="#808040")
    label_prenom.place(relx=0.1,rely=0.1)
    entry_prenom=tk.Entry(formulaire,width=30,textvariable=element_prenom)
    entry_prenom.place(relx=0.22,rely=0.1)
   

    element_age=tk.StringVar()
    label_age=tk.Label(formulaire,text="AGE",bg="#808040")
    label_age.place(relx=0.1,rely=0.15)
    entry_age=tk.Entry(formulaire,width=5,textvariable=element_age)
    entry_age.place(relx=0.16,rely=0.15)
    
    label_classe=tk.Label(formulaire,text="CLASSE",bg="#808040")
    label_classe.place(relx=0.1,rely=0.20)
    classe_liste=[
    "CP1","CP2","CE1","CE2","CM1","CM2","6eme","5eme","4eme","3eme","2nde","1ère","Tl","université"
    ]
    element_classe=tk.StringVar()
    combo_classe=ttk.Combobox(formulaire,values=classe_liste,textvariable=element_classe)
    combo_classe.place(relx=0.2,rely=0.20)
    

    element_sexe=tk.StringVar()
    label_sexe=tk.Label(formulaire,text="_______________SEXE_______________",bg="#808040")
    label_sexe.place(relx=0.1,rely=0.25)
    radiosexeF=tk.Radiobutton(formulaire,variable=element_sexe,text="FEMME",bg="#808040",value="femme")
    radiosexeF.place(relx=0.1,rely=0.30)
    radiosexeM=tk.Radiobutton(formulaire,variable=element_sexe,text="HOMME",bg="#808040",value="homme")
    radiosexeM.place(relx=0.35,rely=0.30)

    element_matricule=tk.StringVar()
    label_matricule=tk.Label(formulaire,text="MATRICULE",bg="#808040")
    label_matricule.place(relx=0.1,rely=0.40)
    entry_matricule=tk.Entry(formulaire,width=15,textvariable= element_matricule)
    entry_matricule.place(relx=0.25,rely=0.40)
   

    element_statut=tk.StringVar()
    label_statut=tk.Label(formulaire,text="______________STATUT______________",bg="#808040")
    label_statut.place(relx=0.1,rely=0.47)
    check_renvoyer=tk.Checkbutton(formulaire,variable=element_statut,text="renvoyé",bg="#808040",onvalue="renvoyé")
    check_renvoyer.place(relx=0.1,rely=0.52)
    check_actif=tk.Checkbutton(formulaire,variable=element_statut,text="actif",bg="#808040",onvalue="actif")
    check_actif.place(relx=0.35,rely=0.52)

    label_mesure=tk.Label(formulaire,text="______________MESURE_____________",bg="#808040")
    label_mesure.place(relx=0.1,rely=0.60)


    label_shirt=tk.Label(formulaire,text="SHIRT",bg="#808040")
    label_shirt.place(relx=0.1,rely=0.65)
    shirt_liste=["M","L","S","XL","XXL"]
    element_shirt=tk.StringVar()
    combo_shirt=ttk.Combobox(formulaire,width=5,values=shirt_liste,textvariable=element_shirt)
    combo_shirt.place(relx=0.18,rely=0.65)
    
    element_shirt=combo_shirt.get()
    label_pointure=tk.Label(formulaire,text="POINTURE",bg="#808040")
    label_pointure.place(relx=0.35,rely=0.65)
    element_pointure=tk.StringVar()
    entry_pointure=tk.Entry(formulaire,width=5,textvariable=element_pointure)
    entry_pointure.place(relx=0.48,rely=0.65)
    

    element_tel=tk.StringVar()
    label_tel=tk.Label(formulaire,text="TEL",bg="#808040")
    label_tel.place(relx=0.1,rely=0.75)
    entry_tel=tk.Entry(formulaire,width=12,textvariable=element_tel)
    entry_tel.place(relx=0.15,rely=0.75)
   
   
   
    button_valider=tk.Button(formulaire,text="VALIDER",width=30,height=3,command=lambda:controleur.ajouter_element(nom=element_nom,prenom=element_prenom,age=element_age,classe=element_classe,sexe=element_sexe,matricule=element_matricule,statut=element_statut,shirt=element_shirt,pointure=element_pointure,tel=element_tel))
    button_valider.place(relx=0.25,rely=0.87)
    return ajouter




