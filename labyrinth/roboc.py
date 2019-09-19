# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""
<<<<<<< HEAD
from resources.carte import Carte
from resources.labyrinthe import Labyrinthe
import os



=======

import os

from carte import Carte
>>>>>>> initial version of labyrinth

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
<<<<<<< HEAD
            labyrinth = Labyrinthe("carlos", contenu)
            cartes.append()
=======
>>>>>>> initial version of labyrinth
            # Création d'une carte, à compléter

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
