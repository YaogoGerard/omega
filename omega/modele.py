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
            age INTEGER,
            classe TEXT,
            sexe INTEGER,
            matricule INTEGER,
            statut INTEGER,
            shirt TEXT,
            pointure INTEGER,
            tel INTEGER);
            """
        )
        self.cur.execute(req)
        self.connexion.commit()

    def ajouter(self, nom, prenom, age, classe, sexe, matricule, statut, shirt, pointure, tel):
        nom_c = str(nom)
        prenom_c = str(prenom)

        classe_c = str(classe)
        sexe_c = str(sexe)

        statut_c = str(statut)
        shirt_c = str(shirt)

        sql = "INSERT INTO beneficiaires(nom,prenom,age,classe,sexe,matricule,statut,shirt,pointure,tel) VALUES(?,?,?,?,?,?,?,?,?,?)"
        data = (nom_c, prenom_c, age, classe_c, sexe_c,
                matricule, statut_c, shirt_c, pointure, tel)
        self.cur.execute(sql, data)
        self.connexion.commit()

    # def arriere(self):
        # self.cur.execute(
            # f"DELETE FROM beneficiaires WHERE ROWID IN (SELECT MAX(ROWID) FROM beneficiaires)")
        # self.connexion.commit()

    def resume(self,type):
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
            print("bonjour")

        elif type=="par Statut":
            actif=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where statut='actif'").fetchone()[0]
            revoyer=self.cur.execute("SELECT COUNT(*) FROM beneficiaires where statut='renvoyé'").fetchone()[0]



    def __del__(self):
        self.connexion.close()
