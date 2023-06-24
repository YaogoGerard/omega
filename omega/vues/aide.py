import tkinter as tk
from tkinter import scrolledtext


def create_frame(parent):
    aide =tk.Frame(parent, bg="#800040")
    message = """Voici une brève aide pour utiliser le logiciel CDE HELP :



1. Fonctionnalités principales :
   - Ajouter un bénéficiaire :
     - Utilisez la méthode `ajouter(nom, prenom, age, classe, sexe, matricule, statut, shirt, pointure, tel)` pour ajouter un bénéficiaire à la base de données.

   - Afficher les bénéficiaires :
     - Utilisez la méthode `afficher(treew, conteneur)` pour afficher les informations d'un bénéficiaire sélectionné dans un widget Treeview.
     - Les informations affichées incluent : nom, prénom, âge, classe, genre, matricule, statut, taille de shirt, pointure de chaussures et numéro de téléphone.

   - Modifier un bénéficiaire :
     - Cliquez sur le bouton "MODIFIER" pour ouvrir une fenêtre de modification.
     - Dans la fenêtre de modification, modifiez les champs nécessaires et cliquez sur le bouton "VALIDER" pour mettre à jour les informations du bénéficiaire.

   - Supprimer un bénéficiaire :
     - Cliquez sur le bouton "SUPPRIMER" pour supprimer le bénéficiaire sélectionné de la base de données.

   - Rechercher des bénéficiaires :
     - Utilisez la méthode `rechercher(entree, treev)` pour rechercher des bénéficiaires en fonction du nom ou du prénom.
     - Les résultats de la recherche seront affichés dans le widget Treeview spécifié.

   - Résumé des bénéficiaires :
     - Utilisez la méthode `resume(type, frame)` pour afficher un résumé des bénéficiaires selon le type spécifié.
     - Les types disponibles sont : "par Age", "par Classe", "par Genre" et "par Statut".
     - Le résumé sera affiché dans le widget Frame spécifié.

2. Utilisation de l'interface utilisateur :
   - L'interface utilisateur contient un widget Treeview pour afficher la liste des bénéficiaires.
   - Vous pouvez sélectionner un bénéficiaire dans le Treeview pour afficher ses informations, les modifier ou le supprimer.
   - Vous pouvez également effectuer des recherches en saisissant un nom ou un prénom dans la zone de recherche.

Note : Assurez-vous d'avoir une connexion à la base de données avant d'utiliser les méthodes mentionnées ci-dessus."""

    
    scrollbar = tk.Scrollbar(aide)
    

    # Créer un widget Text pour afficher le message
    message_text = scrolledtext.ScrolledText(aide, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    message_text.pack(fill=tk.BOTH,expand=True)
    message_text.insert(tk.END, message)

    # Configurer la scrollbar pour faire défiler le widget Text
    scrollbar.config(command=message_text.yview)
    return aide