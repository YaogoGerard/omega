import tkinter as tk
from . import rechercher
from . import ajouter
from . import resume
from . import aide
from . import info

# Création de la fenêtre principale
root = tk.Tk()
root.minsize(width=800,height=600)
# Création du frame de menu
menu_frame = tk.Frame(root,bg="#808040")
menu_frame.pack(side="left",fill="y")
bloc=tk.Frame(menu_frame,bg="#808040")
bloc.pack(pady=250)
# Fonction pour afficher le frame correspondant au bouton cliqué
def show_frame(frame):
	for widget in root.winfo_children():
		if widget is not menu_frame:
			widget.destroy()
			frame.create_frame(root).pack(expand="True",side="left",fill="both")

# Création des trois boutons dans le frame de menu
button1 = tk.Button(bloc, text="RECHERCHER", height = 2, 
          width = 0,bd=0,bg="#808040", command=lambda: show_frame(rechercher))

button1.pack()

button2 = tk.Button(bloc, text="    AJOUTER    ", height = 2, 
          width = 0,bd=0,bg="#808040", command=lambda: show_frame(ajouter))

button2.pack()
button3 = tk.Button(bloc, text="     RESUMÉ     ", height = 2, 
          width = 0,bd=0,bg="#808040", command=lambda: show_frame(resume))
        
button3.pack()

button4 = tk.Button(bloc, text="         AIDE         ", height = 2, 
          width = 0,bd=0,bg="#808040", command=lambda: show_frame(aide))
button4.pack()
button5 = tk.Button(bloc, text="   À PROPOS   ", height = 2, 
          width = 0,bd=0,bg="#808040", command=lambda: show_frame(info))
         
button5.pack()

# Affichage initial du premier frame dans la fenêtre principale
rechercher.create_frame(root).pack(side="left", fill="both", expand=True)

# Affichage de la fenêtre principale
root.mainloop()