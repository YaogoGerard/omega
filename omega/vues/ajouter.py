import tkinter as tk
import tkinter.ttk as ttk
from .. import controleur



def create_frame(parent):
    ajouter= tk.Frame(parent,bg="#800040")
    formulaire=tk.Frame(ajouter,bg="#808040",width=500,height=500)
    formulaire.pack(pady=60)

   
    label_nom=tk.Label(formulaire,text="NOM",bg="#808040")
    label_nom.place(relx=0.1,rely=0.05)
    nom_entry=tk.Entry(formulaire,width=15)
    nom_entry.place(relx=0.18,rely=0.05)
    
    
   
   
    label_prenom=tk.Label(formulaire,text="PRENOM",bg="#808040")
    label_prenom.place(relx=0.1,rely=0.1)
    prenom_entry=tk.Entry(formulaire,width=30)
    prenom_entry.place(relx=0.22,rely=0.1)
   

    
    label_age=tk.Label(formulaire,text="AGE",bg="#808040")
    label_age.place(relx=0.1,rely=0.15)
    age_entry=tk.Entry(formulaire,width=5)
    age_entry.place(relx=0.16,rely=0.15)
    
    label_classe=tk.Label(formulaire,text="CLASSE",bg="#808040")
    label_classe.place(relx=0.1,rely=0.20)
    classe_liste=[
    "CP1","CP2","CE1","CE2","CM1","CM2","6eme","5eme","4eme","3eme","2nde","1ère","Tle","université"
    ]
    
    combo_classe=ttk.Combobox(formulaire,values=classe_liste)
    combo_classe.place(relx=0.2,rely=0.20)
    

    element_sexe=tk.StringVar()
    label_sexe=tk.Label(formulaire,text="_______________SEXE_______________",bg="#808040")
    label_sexe.place(relx=0.1,rely=0.25)
    radiosexeF=tk.Radiobutton(formulaire,variable=element_sexe,text="FEMININ",bg="#808040",value="femme")
    radiosexeF.place(relx=0.1,rely=0.30)
    radiosexeM=tk.Radiobutton(formulaire,variable=element_sexe,text="MASCULIN",bg="#808040",value="homme")
    radiosexeM.place(relx=0.35,rely=0.30)

  
    label_matricule=tk.Label(formulaire,text="MATRICULE",bg="#808040")
    label_matricule.place(relx=0.1,rely=0.40)
    matricule_entry=tk.Entry(formulaire,width=15)
    matricule_entry.place(relx=0.25,rely=0.40)
   

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
    
    combo_shirt=ttk.Combobox(formulaire,width=5,values=shirt_liste)
    combo_shirt.place(relx=0.18,rely=0.65)
    
    
    label_pointure=tk.Label(formulaire,text="POINTURE",bg="#808040")
    label_pointure.place(relx=0.35,rely=0.65)
    
    pointure_entry=tk.Entry(formulaire,width=5)
    pointure_entry.place(relx=0.48,rely=0.65)
    

   
    label_tel=tk.Label(formulaire,text="TEL",bg="#808040")
    label_tel.place(relx=0.1,rely=0.75)
    tel_entry=tk.Entry(formulaire,width=12)
    tel_entry.place(relx=0.15,rely=0.75)
   
   
   
    button_valider=tk.Button(formulaire,text="VALIDER",width=30,height=3,command=lambda:controleur.ajouter_element(nom=nom_entry.get(),prenom=prenom_entry.get(),age=age_entry.get(),classe=combo_classe.get(),sexe=element_sexe.get(),matricule=matricule_entry.get(),statut=element_statut.get(),shirt=combo_shirt.get(),pointure=pointure_entry.get(),tel=tel_entry.get(),a=nom_entry,b=prenom_entry,c=age_entry,d=combo_classe,e=radiosexeF,f=radiosexeM,g=matricule_entry,h=check_renvoyer,i=check_actif,j=combo_shirt,k=pointure_entry,l=tel_entry))
    button_valider.place(relx=0.25,rely=0.87)
    return ajouter




