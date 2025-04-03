# Importation des modules
import os
import tkinter as tk
from tkinter import PhotoImage
from random import choice

# Définition des actions
ACTIONS = ['Pierre', 'Papier', 'Ciseaux']

# Fonction jeu pour le jeu Pierre-Papier-Ciseaux
def jeu(choix_joueur):
    # Nom du joueur
    nom = champ_nom.get() if champ_nom.get() else "Joueur"

    # Choix aléatoire de l'ordinateur
    choix_ordi = choice(ACTIONS)

    # Déterminer le gagnant
    if (choix_joueur == choix_ordi):
        resultat = "Egalité !"
    elif (choix_joueur == "Pierre" and choix_ordi == "Ciseaux" or
          choix_joueur == "Papier" and choix_ordi == "Pierre" or
          choix_joueur == "Ciesaux" and choix_ordi == "Papier"):
        resultat = nom + " a gagné !"
    else:
        resultat = "L'ordinateur a gagné !"

    # Mise à jour des images et du texte
    label_joueur.config(image=images[choix_joueur])
    label_ordi.config(image=images[choix_ordi])
    label_resultat.config(text=resultat)

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Pierre - Papier - Ciseaux")
fenetre.geometry("500x400")

# Chargement des images
images = {
    'Pierre': PhotoImage(file='images/pierre.png'),
    'Papier': PhotoImage(file='images/papier.png'),
    'Ciseaux': PhotoImage(file='images/ciseaux.png')
}

# Input du nom du joueur
label_nom = tk.Label(fenetre, text="Entrez votre nom :", font=("Arial", 12))
label_nom.pack()
champ_nom = tk.Entry(fenetre, font=("Arial", 12))
champ_nom.pack()

# Label pour afficher le choix du joueur et de l'ordinateur
frame_choix = tk.Frame(fenetre)
frame_choix.pack(pady=10)

label_joueur = tk.Label(frame_choix, text="Ton choix :", font=("Arial", 12))
label_joueur.pack(side="left", padx=20)
label_ordi = tk.Label(frame_choix, text="Choix de l'ordinateur :", font=("Arial", 12))
label_ordi.pack(side="right", padx=20)

# Boutons des images
frame_buttons = tk.Frame(fenetre)
frame_buttons.pack(pady=10)

for choix in ACTIONS:
    bouton = tk.Button(frame_buttons, image=images[choix], command=lambda c=choix: jeu(c))
    bouton.pack(side="left", padx=10)

# Label pour afficher le résultat
label_resultat = tk.Label(fenetre, text="", font=("Arial", 14), fg="blue")
label_resultat.pack(pady=10)

# Lancer le jeu
fenetre.mainloop()