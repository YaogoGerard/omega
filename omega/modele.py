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

    def ajouter(self, nom, prenom, age, classe, sexe, matricule, statut, shirt, pointure, tel):
       

        sql = "INSERT INTO beneficiaires(nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel) VALUES(?,?,?,?,?,?,?,?,?,?)"
        data = (nom , prenom, age, classe, sexe,
                matricule, statut, shirt, pointure, tel)
        self.cur.execute(sql, data)
        self.connexion.commit()

    # def arriere(self):
        # self.cur.execute(
            # f"DELETE FROM beneficiaires WHERE ROWID IN (SELECT MAX(ROWID) FROM beneficiaires)")
        # self.connexion.commit()

    def resume(self,type,frame):
        if type=="par Age":
            

            cinq=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='5'").fetchone()[0]
            six=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='6'").fetchone()[0]
            sept=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='7'").fetchone()[0]
            huit=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='8'").fetchone()[0]
            neuf=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='9'").fetchone()[0]
            dix=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='10'").fetchone()[0]
            onze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='11'").fetchone()[0]
            douze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='12'").fetchone()[0]
            treize=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='13'").fetchone()[0]
            quatorze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='14'").fetchone()[0]
            quinze=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='15'").fetchone()[0]
            seize=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='16'").fetchone()[0]
            dix_sept=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='17'").fetchone()[0]
            dix_huit=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='18'").fetchone()[0]
            dix_neuf=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='19'").fetchone()[0]
            vingt=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='20'").fetchone()[0]
            vingt_un=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='21'").fetchone()[0]
            vingt_deux=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where age='22'").fetchone()[0]
        elif type=="par sexe":
            femme=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where sexe='femme'").fetchone()[0]
            homme=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where sexe='homme'").fetchone()[0]  
        elif type=="par Shirt":
            M=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='M'").fetchone()[0]
            L=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='L'").fetchone()[0]
            XL=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='XL'").fetchone()[0]
            XXL=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where shirt='XXL'").fetchone()[0]
        elif type=="par Pointure":
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
            actif=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where statut='actif'").fetchone()[0]
            revoyer=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where statut='renvoyé'").fetchone()[0]

        

    def __del__(self):
        self.connexion.close()
