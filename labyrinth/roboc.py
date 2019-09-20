#-*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from resources.carte import Carte
from resources.labyrinthe import Labyrinthe

# On charge les cartes existantes
cartes = []
nom_robot = input("Insert the name of yout robot:\n")
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            carte = Carte(nom_carte, contenu)
            cartes.append(carte)
            laby = Labyrinthe(nom_robot, carte.labyrinthe)
            # Création d'une carte, à compléter
            print(laby)
# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
