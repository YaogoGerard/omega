import sqlite3
import tkinter as tk
import os
from tkinter import ttk
from tkinter import messagebox

# creation d'une classe pour la base de données


class database:
    def __init__(self):
        self.db_name = "OMEGA_DATA.db"
        self.path = os.path.join(os.path.dirname(__file__), self.db_name)
        self.connexion = sqlite3.connect(self.path)
        self.cur = self.connexion.cursor()
        req = (
            """
            CREATE TABLE IF NOT EXISTS beneficiaires(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            nom TEXT,
            prenom TEXT,
            age TEXT,
            classe TEXT,
            sexe TEXT,
            matricule TEXT,
            statut TEXT,
            shirt TEXT,
            pointure TEXT,
            tel TEXTE);
            """
        )
        self.cur.execute(req)
        self.connexion.commit()

    
     
    def afficher(self,treew,conteneur):
       
        valeur=treew.item(treew.selection())["text"]
        nom,prenom=valeur.split(" ")
        self.cur.execute("SELECT nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel,id FROM beneficiaires WHERE nom=? AND prenom=?",(nom,prenom))
        donnees=self.cur.fetchall()
        
        label_nom=tk.Label(conteneur,text="NOM: "+donnees[0][0])
        label_nom.pack()
        label_prenom=tk.Label(conteneur,text="PRENOM: "+donnees[0][1])
        label_prenom.pack()
        label_age=tk.Label(conteneur,text="AGE: "+donnees[0][2])
        label_age.pack()
        label_classe=tk.Label(conteneur,text="CLASSE: "+donnees[0][3])
        label_classe.pack()
        label_genre=tk.Label(conteneur,text="GENRE: "+donnees[0][4])
        label_genre.pack()
        label_matricule=tk.Label(conteneur,text="MATRICULE: "+donnees[0][5])
        label_matricule.pack()
        label_statut=tk.Label(conteneur,text="STATUT: "+donnees[0][6])
        label_statut.pack()
        label_shirt=tk.Label(conteneur,text="SHIRT: "+donnees[0][7])
        label_shirt.pack()
        label_pointure=tk.Label(conteneur,text="POINTURE: "+donnees[0][8])
        label_pointure.pack()
        label_tel=tk.Label(conteneur,text="TELEPHONE: "+donnees[0][9])
        label_tel.pack()

        def modifier(boite):
            changement = tk.Toplevel(boite, bg="#808040", width=500,height=500)
            changement.pack_propagate()
            label_nom = tk.Label(changement, text="NOM", bg="#808040")
            label_nom.place(relx=0.1, rely=0.05)
            nom_entry = tk.Entry(changement, width=15)
            nom_entry.insert(0,donnees[0][0])
            nom_entry.place(relx=0.18, rely=0.05)

            label_prenom = tk.Label(changement, text="PRENOM", bg="#808040")
            label_prenom.place(relx=0.1, rely=0.1)
            prenom_entry = tk.Entry(changement, width=30)
            prenom_entry.insert(0,donnees[0][1])
            prenom_entry.place(relx=0.22, rely=0.1)

            label_age = tk.Label(changement, text="AGE", bg="#808040")
            label_age.place(relx=0.1, rely=0.15)
            age_entry = tk.Entry(changement, width=5)
            age_entry.insert(0,donnees[0][2])
            age_entry.place(relx=0.16, rely=0.15)

            label_classe = tk.Label(changement, text="CLASSE", bg="#808040")
            label_classe.place(relx=0.1, rely=0.20)
            classe_liste = [
                "CP1", "CP2", "CE1", "CE2", "CM1", "CM2", "6eme", "5eme", "4eme", "3eme", "2nde", "1ère", "Tle", "université"
            ]
            combo_classe = ttk.Combobox(changement, values=classe_liste)
            combo_classe.set(donnees[0][3])
            combo_classe.place(relx=0.2, rely=0.20)

            element_sexe = tk.StringVar()
            
            label_sexe = tk.Label(
                changement, text="_______________SEXE_______________", bg="#808040")
            label_sexe.place(relx=0.1, rely=0.25)
            radiosexeF = tk.Radiobutton(
                changement, variable=element_sexe, text="FEMININ", bg="#808040", value="femme")
            radiosexeF.place(relx=0.1, rely=0.30)
            radiosexeM = tk.Radiobutton(
                changement, variable=element_sexe, text="MASCULIN", bg="#808040", value="homme")
            radiosexeM.place(relx=0.35, rely=0.30)
            

            label_matricule = tk.Label(
                changement, text="MATRICULE", bg="#808040")
            label_matricule.place(relx=0.1, rely=0.40)
            matricule_entry = tk.Entry(changement, width=15)
            matricule_entry.insert(0,donnees[0][5])
            matricule_entry.place(relx=0.25, rely=0.40)

            element_statut = tk.StringVar()
            label_statut = tk.Label(
                changement, text="______________STATUT______________", bg="#808040")
            label_statut.place(relx=0.1, rely=0.47)
            check_renvoyer = tk.Checkbutton(
                changement, variable=element_statut, text="renvoyé", bg="#808040", onvalue="renvoyé")
            check_renvoyer.place(relx=0.1, rely=0.52)
            check_actif = tk.Checkbutton(
                changement, variable=element_statut, text="actif", bg="#808040", onvalue="actif")
            check_actif.place(relx=0.35, rely=0.52)
            

            label_mesure = tk.Label(
                changement, text="______________MESURE_____________", bg="#808040")
            label_mesure.place(relx=0.1, rely=0.60)

            label_shirt = tk.Label(changement, text="SHIRT", bg="#808040")
            label_shirt.place(relx=0.1, rely=0.65)
            shirt_liste = ["M", "L", "S", "XL", "XXL"]

            combo_shirt = ttk.Combobox(changement, width=5, values=shirt_liste)
            combo_shirt.set(donnees[0][7])
            combo_shirt.place(relx=0.18, rely=0.65)

            label_pointure = tk.Label(
                changement, text="POINTURE", bg="#808040")
            label_pointure.place(relx=0.35, rely=0.65)

            pointure_entry = tk.Entry(changement, width=5)
            pointure_entry.insert(0,donnees[0][8])
            pointure_entry.place(relx=0.48, rely=0.65)

            label_tel = tk.Label(changement, text="TEL", bg="#808040")
            label_tel.place(relx=0.1, rely=0.75)
            tel_entry = tk.Entry(changement, width=12)
            tel_entry.insert(0,donnees[0][9])
            tel_entry.place(relx=0.15, rely=0.75)
            annuler= tk.Button(changement, text="ANNULER", command=lambda:changement.destroy())
            annuler.place(relx=0.15, rely=0.90)
            valider= tk.Button(changement, text="VALIDER",command=lambda:validation())
            valider.place(relx=0.75, rely=0.90)
            def validation():
                nouveau_nom = nom_entry.get()
                nouveau_prenom = prenom_entry.get()
                nouveau_age = age_entry.get()
                nouveau_classe = combo_classe.get()
                nouveau_matricule = matricule_entry.get()             
                nouveau_shirt = combo_shirt.get()
                nouveau_pointure = pointure_entry.get()
                nouveau_tel = tel_entry.get()

                
                self.cur.execute("UPDATE beneficiaires SET nom=?, prenom=?, age=?, classe=?, matricule=?,shirt=?, pointure=?, tel=? WHERE nom=? AND prenom=?",
                                (nouveau_nom, nouveau_prenom, nouveau_age, nouveau_classe, nouveau_matricule, nouveau_shirt, nouveau_pointure, nouveau_tel, nom, prenom))
                self.connexion.commit()
                changement.destroy()
                
               
                changement.destroy()

                messagebox.showinfo("Mise à jour réussie", "Les informations ont été mises à jour avec succès.")
                treew.delete(*treew.get_children())
                self.cur.execute("SELECT nom, prenom FROM beneficiaires")
                donnees = self.cur.fetchall()
                for element in donnees:
                    nom_prenom = element[0] + " " + element[1]
                    treew.insert("", "end", text=nom_prenom)
                for widget in conteneur.winfo_children():
                    widget.destroy()
                
                
                



        def supprimer():
            self.cur.execute("DELETE FROM beneficiaires WHERE nom=? AND prenom=?", (nom, prenom))
            root=tk.Tk()
            root.withdraw()
            messagebox.showinfo("Suppression réussie", "Le bénéficiaire a été supprimé avec succès.")
            root.destroy()
            for item in treew.get_children():
                treew.delete(item)
            self.cur.execute("SELECT nom,prenom FROM beneficiaires")
            donnees=self.cur.fetchall()
            for element in donnees:
                nom_prenom=element[0]+" "+element[1]
                treew.insert("","end",text=nom_prenom)
            
            
        modifie = tk.Button(conteneur, text="MODIFIER",command=lambda: modifier(conteneur))
        modifie.pack(side="left")
        supprime = tk.Button(conteneur, text="SUPPRIMER", command=lambda:supprimer())
        supprime.pack(side="right")

    def rechercher(self,entree,treev):
        
        if not entree:
            self.cur.execute("SELECT nom, prenom FROM beneficiaires ")
            treev.delete(*treev.get_children())
            donnees=self.cur.fetchall()
            for element in donnees:
                nom_prenom=element[0]+" "+element[1]
                treev.insert("","end",text=nom_prenom)
        else:
            self.cur.execute("SELECT nom, prenom FROM beneficiaires WHERE nom LIKE ? or prenom LIKE ?",(f'{entree}%',f'{entree}%'))
            treev.delete(*treev.get_children())
            for row in self.cur.fetchall():
                nom_prenom=f'{row[0]} {row[1]}'
                treev.insert("","end",text=nom_prenom)


    def remplir_treeview(self,tree):
        for row in tree.get_children():
            tree.delete(row) 
        self.cur.execute("SELECT nom,prenom FROM beneficiaires")
        donnees=self.cur.fetchall()
        for element in donnees:
            nom_prenom=element[0]+" "+element[1]
            tree.insert("","end",text=nom_prenom)
    

    def ajouter(self, nom, prenom, age, classe, sexe, matricule, statut, shirt, pointure, tel):
        nom=str(nom)
        prenom=str(prenom)
        age=str(age)
        classe=str(classe)
        sexe=str(sexe)
        matricule=str(matricule)
        statut=str(statut)
        shirt=str(shirt)
        pointure=str(pointure)
        tel=str(tel)

        sql = "INSERT INTO beneficiaires(nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel) VALUES(?,?,?,?,?,?,?,?,?,?)"
        data = (nom , prenom, age, classe, sexe,
                matricule, statut, shirt, pointure, tel)
        self.cur.execute(sql, data)
        self.connexion.commit()

   
    def resume(self,type,frame):
        type=str(type)
        if type=="par Age":
            titre_age=tk.Label(frame,text="**********PAR AGE**********")
            titre_age.place(x=220,y=10)

            cinq=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='5'").fetchone()[0]
            cinq_number=tk.Label(frame,text="5 ANS : "+str(cinq))
            cinq_number.place(x=250,y=30)
            
            six=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='6'").fetchone()[0]
            six_number=tk.Label(frame,text="6 ANS : "+str(six))
            six_number.place(x=250,y=45)

            sept=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='7'").fetchone()[0]
            sept_number=tk.Label(frame,text="7 ANS : "+str(sept))
            sept_number.place(x=250,y=60)

            huit=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='8'").fetchone()[0]
            huit_number=tk.Label(frame,text="8 ANS : "+str(huit))
            huit_number.place(x=250,y=75)

            neuf=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='9'").fetchone()[0]
            neuf_number=tk.Label(frame,text="9 ANS : "+str(neuf))
            neuf_number.place(x=250,y=90)

            dix=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='10'").fetchone()[0]
            dix_number=tk.Label(frame,text="10 ANS : "+str(dix))
            dix_number.place(x=250,y=105)

            onze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='11'").fetchone()[0]
            onze_number=tk.Label(frame,text="11 ANS : "+str(onze))
            onze_number.place(x=250,y=120)

            douze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='12'").fetchone()[0]
            douze_number=tk.Label(frame,text="12 ANS : "+str(douze))
            douze_number.place(x=250,y=135)

            treize=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='13'").fetchone()[0]
            treize_number=tk.Label(frame,text="13 ANS : "+str(treize))
            treize_number.place(x=250,y=150)

            quatorze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='14'").fetchone()[0]
            quatorze_number=tk.Label(frame,text="14 ANS : "+str(quatorze))
            quatorze_number.place(x=250,y=165)

            quinze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='15'").fetchone()[0]
            quinze_number=tk.Label(frame,text="15 ANS : "+str(quinze))
            quinze_number.place(x=250,y=180)

            seize=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='16'").fetchone()[0]
            seize_number=tk.Label(frame,text="16 ANS : "+str(seize))
            seize_number.place(x=250,y=195)

            dix_sept=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='17'").fetchone()[0]
            dix_sept_number=tk.Label(frame,text="17 ANS : "+str(dix_sept))
            dix_sept_number.place(x=250,y=210)

            dix_huit=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='18'").fetchone()[0]
            dix_huit_number=tk.Label(frame,text="18 ANS : "+str(dix_huit))
            dix_huit_number.place(x=250,y=225)
            
            dix_neuf=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='19'").fetchone()[0]
            dix_neuf_number=tk.Label(frame,text="19 ANS : "+str(dix_neuf))
            dix_neuf_number.place(x=250,y=240)

            vingt=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='20'").fetchone()[0]
            vingt_number=tk.Label(frame,text="20 ANS : "+str(vingt))
            vingt_number.place(x=250,y=255)

            vingt_un=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='21'").fetchone()[0]
            vingt_un_number=tk.Label(frame,text="21 ANS : "+str(vingt_un))
            vingt_un_number.place(x=250,y=270)

            vingt_deux=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='22'").fetchone()[0]
            vingt_deux_number=tk.Label(frame,text="22 ANS : "+str(vingt_deux))
            vingt_deux_number.place(x=250,y=285)

        elif type=="par Genre":
            titre_sexe=tk.Label(frame,text="***********PAR GENRE**********")
            titre_sexe.place(x=210,y=10)
            femme=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where sexe='femme'").fetchone()[0]
            femme_number=tk.Label(frame,text="FEMME : "+str(femme))
            femme_number.place(x=250,y=50)
            homme=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where sexe='homme'").fetchone()[0] 
            homme_number=tk.Label(frame,text="HOMME : "+str(homme))
            homme_number.place(x=250,y=90) 
        elif type=="par Shirt":
            titre_shirt=tk.Label(frame,text="**********PAR SHIRT**********")
            titre_shirt.place(x=210,y=20)
            M=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='M'").fetchone()[0]
            M_number=tk.Label(frame,text="shirt M : "+str(M))
            M_number.place(x=250,y=50)
            L=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='L'").fetchone()[0]
            L_number=tk.Label(frame,text="shirt L : "+str(L))
            L_number.place(x=250,y=70)
            XL=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='XL'").fetchone()[0]
            XL_number=tk.Label(frame,text="shirt XL : "+str(XL))
            XL_number.place(x=250,y=90)
            XXL=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='XXL'").fetchone()[0]
            XXL_number=tk.Label(frame,text="Shirt XXL: "+str(XXL))
            XXL_number.place(x=250,y=110)
        elif type=="par Pointure":
            titre_pointure=tk.Label(frame,text="**********PAR POINTURE**********")
            titre_pointure.place(x=210,y=7)
            p20=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='20'").fetchone()[0]
            p20_number=tk.Label(frame,text="pointure 20 : "+str(p20))
            p20_number.place(x=250,y=27)
            
            p22=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='22'").fetchone()[0]
            p22_number=tk.Label(frame,text="Pointure 22:" +str(p22))
            p22_number.place(x=250,y=45)
            
            p24=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='24'").fetchone()[0]
            p24_number=tk.Label(frame,text="Pointure 24:" +str(p24))
            p24_number.place(x=250,y=60)

            p25=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='25'").fetchone()[0]
            p25_number=tk.Label(frame,text="Pointure 25:" +str(p25))
            p25_number.place(x=250,y=75)

            p26=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='26'").fetchone()[0]
            p26_number=tk.Label(frame,text="Pointure 26:" +str(p26))
            p26_number.place(x=250,y=90)

            p27=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='27'").fetchone()[0]
            p27_number=tk.Label(frame,text="Pointure 27:" +str(p27))
            p27_number.place(x=250,y=105)

            p28=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='28'").fetchone()[0]
            p28_number=tk.Label(frame,text="Pointure 28:" +str(p28))
            p28_number.place(x=250,y=120)

            p29=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='29'").fetchone()[0]
            p29_number=tk.Label(frame,text="Pointure 29:" +str(p29))
            p29_number.place(x=250,y=135)

            p30=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='30'").fetchone()[0]
            p30_number=tk.Label(frame,text="Pointure 30:" +str(p30))
            p30_number.place(x=250,y=150)

            p31=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='31'").fetchone()[0]
            p31_number=tk.Label(frame,text="Pointure 31: "+str(p31))
            p31_number.place(x=250,y=165)

            p32=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='32'").fetchone()[0]
            p32_number=tk.Label(frame,text="Pointure 32: "+str(p32))
            p32_number.place(x=250,y=180)
           
            p34=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='34'").fetchone()[0]
            p34_number=tk.Label(frame,text="Pointure 34: "+str(p34))
            p34_number.place(x=250,y=195)

            p35=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='35'").fetchone()[0]
            p35_number=tk.Label(frame,text="Pointure 35: "+str(p35))
            p35_number.place(x=250,y=210)

            p37=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='37'").fetchone()[0]
            p37_number=tk.Label(frame,text="Pointure 37: "+str(p37))
            p37_number.place(x=250,y=225)

            p38=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='38'").fetchone()[0]
            p38_number=tk.Label(frame,text="Pointure 38: "+str(p38))
            p38_number.place(x=250,y=240)

            p39=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='39'").fetchone()[0]
            p39_number=tk.Label(frame,text="Pointure 39: "+str(p39))
            p39_number.place(x=250,y=255)

            p40=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='40'").fetchone()[0]
            p40_number=tk.Label(frame,text="Pointure 40: "+str(p40))
            p40_number.place(x=250,y=270)

            p42=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='42'").fetchone()[0]
            p42_number=tk.Label(frame,text="Pointure 42: "+str(p42))
            p42_number.place(x=250,y=285)

            p43=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='43'").fetchone()[0]
            p43_number=tk.Label(frame,text="Pointure 43: "+str(p43))
            p43_number.place(x=250,y=300)

            p44=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='44'").fetchone()[0]
            p44_number=tk.Label(frame,text="Pointure 44: "+str(p44))
            p44_number.place(x=250,y=315)

            p45=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='45'").fetchone()[0]
            p45_number=tk.Label(frame,text="Pointure 45: "+str(p45))
            p45_number.place(x=250,y=330)

            p46=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='46'").fetchone()[0]
            p46_number=tk.Label(frame,text="Pointure 46: "+str(p46))
            p46_number.place(x=250,y=345)

            p47=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='47'").fetchone()[0]
            p47_number=tk.Label(frame,text="Pointure 47: "+str(p47))
            p47_number.place(x=250,y=360)

            p48=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='48'").fetchone()[0]
            p48_number=tk.Label(frame,text="Pointure 48: "+str(p48))
            p48_number.place(x=250,y=375)

            p49=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='49'").fetchone()[0]
            p49_number=tk.Label(frame,text="Pointure 49: "+str(p49))
            p49_number.place(x=250,y=390)

            p50=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='50'").fetchone()[0]
            p50_number=tk.Label(frame,text="Pointure 50: "+str(p50))
            p50_number.place(x=250,y=405)

        elif type=="par Statut":
            titre_statut=tk.Label(frame,text="*********PAR STATUT**********")
            titre_statut.place(x=250,y=10)
            actif=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where statut='actif'").fetchone()[0]
            actif_number=tk.Label(frame,text="Actifs: "+ str(actif))
            actif_number.place(x=250,y=30)
            renvoyer=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where statut='renvoyé'").fetchone()[0]
            renvoyer_number=tk.Label(frame,text="Renvoyés: "+str(renvoyer))
            renvoyer_number.place(x=250,y=45)

        

    def __del__(self):
        self.connexion.close()
