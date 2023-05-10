import sqlite3
import tkinter as tk
import os
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
            titre_age.pack()

            cinq=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='5'").fetchone()[0]
            cinq_number=tk.Label(frame,text="5 ANS : "+str(cinq))
            cinq_number.place(x=400,y=30)
            
            six=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='6'").fetchone()[0]
            six_number=tk.Label(frame,text="6 ANS : "+str(six))
            six_number.place(x=400,y=45)

            sept=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='7'").fetchone()[0]
            sept_number=tk.Label(frame,text="7 ANS : "+str(sept))
            sept_number.place(x=400,y=60)

            huit=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='8'").fetchone()[0]
            huit_number=tk.Label(frame,text="8 ANS : "+str(huit))
            huit_number.place(x=400,y=75)

            neuf=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='9'").fetchone()[0]
            neuf_number=tk.Label(frame,text="9 ANS : "+str(neuf))
            neuf_number.place(x=400,y=90)

            dix=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='10'").fetchone()[0]
            dix_number=tk.Label(frame,text="10 ANS : "+str(dix))
            dix_number.place(x=400,y=105)

            onze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='11'").fetchone()[0]
            onze_number=tk.Label(frame,text="11 ANS : "+str(onze))
            onze_number.place(x=400,y=120)

            douze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='12'").fetchone()[0]
            douze_number=tk.Label(frame,text="12 ANS : "+str(douze))
            douze_number.place(x=400,y=135)

            treize=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='13'").fetchone()[0]
            treize_number=tk.Label(frame,text="13 ANS : "+str(treize))
            treize_number.place(x=400,y=150)

            quatorze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='14'").fetchone()[0]
            quatorze_number=tk.Label(frame,text="14 ANS : "+str(quatorze))
            quatorze_number.place(x=400,y=165)

            quinze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='15'").fetchone()[0]
            quinze_number=tk.Label(frame,text="15 ANS : "+str(quinze))
            quinze_number.place(x=400,y=180)

            seize=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='16'").fetchone()[0]
            seize_number=tk.Label(frame,text="16 ANS : "+str(seize))
            seize_number.place(x=400,y=195)

            dix_sept=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='17'").fetchone()[0]
            dix_sept_number=tk.Label(frame,text="17 ANS : "+str(dix_sept))
            dix_sept_number.place(x=400,y=210)

            dix_huit=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='18'").fetchone()[0]
            dix_huit_number=tk.Label(frame,text="18 ANS : "+str(dix_huit))
            dix_huit_number.place(x=400,y=225)
            
            dix_neuf=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='19'").fetchone()[0]
            dix_neuf_number=tk.Label(frame,text="19 ANS : "+str(dix_neuf))
            dix_neuf_number.place(x=400,y=240)

            vingt=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='20'").fetchone()[0]
            vingt_number=tk.Label(frame,text="20 ANS : "+str(vingt))
            vingt_number.place(x=400,y=255)

            vingt_un=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='21'").fetchone()[0]
            vingt_un_number=tk.Label(frame,text="21 ANS : "+str(vingt_un))
            vingt_un_number.place(x=400,y=270)

            vingt_deux=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='22'").fetchone()[0]
            vingt_deux_number=tk.Label(frame,text="22 ANS : "+str(vingt_deux))
            vingt_deux_number.place(x=400,y=285)

        elif type=="par Genre":
            titre_sexe=tk.Label(frame,text="***********PAR GENRE**********")
            titre_sexe.place(x=300,y=10)
            femme=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where sexe='femme'").fetchone()[0]
            femme_number=tk.Label(frame,text="FEMME : "+str(femme))
            femme_number.place(x=300,y=50)
            homme=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where sexe='homme'").fetchone()[0] 
            homme_number=tk.Label(frame,text="HOMME : "+str(homme))
            homme_number.place(x=300,y=90) 
        elif type=="par Shirt":
            titre_shirt=tk.Label(frame,text="**********PAR SHIRT**********")
            titre_shirt.place(x=400,y=20)
            M=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='M'").fetchone()[0]
            M_number=tk.Label(frame,text="shirt M : "+str(M))
            M_number.place(x=400,y=50)
            L=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='L'").fetchone()[0]
            L_number=tk.Label(frame,text="shirt L : "+str(L))
            L_number.place(x=400,y=70)
            XL=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='XL'").fetchone()[0]
            XL_number=tk.Label(frame,text="shirt XL : "+str(XL))
            XL_number.place(x=400,y=90)
            XXL=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='XXL'").fetchone()[0]
            XXL_number=tk.Label(frame,text="shirt XXL : "+str(XXL))
            XXL_number.place(x=400,y=105)
        elif type=="par Pointure":
            titre_pointure=tk.Label(frame,text="PAR POINTURE",bg="#800040")
            titre_pointure.pack()
            p20=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='20'").fetchone()[0]
            
            p22=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='22'").fetchone()[0]
            
            p24=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='24'").fetchone()[0]
            p25=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='25'").fetchone()[0]
            p26=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='26'").fetchone()[0]
            p27=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='27'").fetchone()[0]
            p28=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='28'").fetchone()[0]
            p29=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='29'").fetchone()[0]
            p30=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='30'").fetchone()[0]
            p31=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='31'").fetchone()[0]
            p32=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='32'").fetchone()[0]
           
            p34=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='34'").fetchone()[0]
            p35=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='35'").fetchone()[0]

            p37=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='37'").fetchone()[0]
            p38=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='38'").fetchone()[0]
            p39=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='39'").fetchone()[0]
            p40=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='40'").fetchone()[0]

            p42=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='42'").fetchone()[0]
            p43=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='43'").fetchone()[0]
            p44=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='44'").fetchone()[0]
            p45=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='45'").fetchone()[0]
            p46=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='46'").fetchone()[0]
            p47=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='47'").fetchone()[0]
            p48=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='48'").fetchone()[0]
            p49=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='49'").fetchone()[0]
            p50=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where pointure='50'").fetchone()[0]

        elif type=="par Statut":
            titre_statut=tk.Label(frame,text="*********PAR STATUT**********")
            titre_statut.place(x=350,y=100)
            actif=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where statut='actif'").fetchone()[0]
            actif_number=tk.Label(frame,text="Actifs: "+ str(actif))
            actif_number.place(x=300,y=200)
            renvoyer=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where statut='renvoyé'").fetchone()[0]
            renvoyer_number=tk.Label(frame,text="Renvoyés: "+str(renvoyer))
            renvoyer_number.place(x=500,y=200)

        

    def __del__(self):
        self.connexion.close()
