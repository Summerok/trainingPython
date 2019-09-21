#-*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import re

from resources.carte import Carte
from resources.labyrinthe import Labyrinthe

# On charge les cartes existantes
cartes = []
nom_robot = input("Insert the name of your robot:\n")
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            carte = Carte(nom_carte, contenu)
            cartes.append(carte)
            #laby = Labyrinthe(nom_robot, carte.labyrinthe)
# Création d'une carte, à compléter
print("You can create and edit your own cartes, just by typing\
a .txt with the labyrinth")
print("Nota: Borders are always limited either by O 'obstacle' or U 'exit'")
os.system("pause")
            #print(laby)
#laby.save_your_game()
#laby1 = laby.load_last_game()
#print(laby1)


# On affiche les cartes existantes
print("Existing labyrinths :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée,
laby = Labyrinthe(nom_robot, {})
if laby.load_last_game():
    print("  s - Saved game")

# Tant qu'on ne sélectionne une carte disponible,
# on reste dans la boucle while
selection = "" 
retry = True
while retry:
    selection = input("Choose your game to start playing: ")
    try:
        selection = int(selection)
    except ValueError:
        if laby.load_last_game() and selection == "s":
            laby = laby.load_last_game()
            retry = False
        else:
            print("You did a wrong selection!")
    else:
        try:
            cartes[selection-1]
        except IndexError:
            print("You did a wrong selection!")    
        else:
            if selection > 0:
                laby.grille = cartes[selection-1].labyrinthe
                laby.fill_doors()
                retry = False
            else:
                print("You did a wrong selection!")

# ... Complétez le programme ...
print("")
print(laby)
print("")
game_continue = True
while game_continue:
    laby.save_your_game()
    movement = input("> ")
    laby.move_robot(movement)
