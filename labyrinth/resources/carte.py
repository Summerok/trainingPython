# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""
    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        """Retourner le nom de la carte definie"""
        return "<Carte {}>".format(self.nom)

    def creer_labyrinthe_depuis_chaine(self, chaine):
        """Decode carte in a dictionary data structure with 2 axis (x, y)
        starting by (0, 0)"""
        labyLoad = {}
        y = 0
        x = 0
        for obj in chaine:
            if obj == "\n":
                labyLoad[x, y] = obj
                y += 1
                x = 0
            else:
                labyLoad[x, y] = obj
                x += 1
        return labyLoad