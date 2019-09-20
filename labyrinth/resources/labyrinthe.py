# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = obstacles
        # ...
    def __str__(self):
        liste = []
        for obj in self.grille.values:
            liste.append(obj)
        return liste