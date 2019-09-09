#!/usr/local/bin/python3
# -*-coding:Latin-1 -*
class SortDict:
    '''Classe définissant un dictionnaire ordonné'''
    def __init__(self, base = {}, **donnees):
        """Ce constructeur permet d'initialiser de trois 
        façons differentes"""
        self._cles = []
        self._valeurs = []
        if type(base) not in (dict, SortDict):
            raise TypeError("le type attendu est un dictionnaire (usuel ou ordonne)")

        for cle in base: 
            self[cle] = base[cle]

        for cle in donnees:
            self[cle] = donnees[cle]
    def __setitem__(self, cle, valeur):
        """Cette méthode de conteneur d'objets permet
        d'ajouter une cle, valeur à la fin de la liste de cles et de valeurs si ce pair n'existait pas ou
        d'ajouter une valeur au même indice que la cle correspondante"""
        if cle in self._cles:
            indice = self._cles.index(cle)
            self._valeurs[indice] = valeur
        else:
            self._cles.append(cle)
            self._valeurs.append(valeur)
    def __getitem__(self, cle):
        """Méthode qui récupère une valeur de la liste _valeurs au même indice de la cle si celle-ci existe"""
        if cle in self._cles:
            indice = self._cles.index(cle)
            return self._valeurs[indice]
        else:
            raise LookupError("La clé n'est pas trouvée")
    def __repr__(self):
        """Méthode qui permet d'afficher l'objet lorsqu'on tape son nom"""
        taille = len(self._cles)
        if taille > 1:
            affiche = "{"
            i=0
            while i < (len(self._cles) - 1):
                affiche = affiche + "'" + str(self._cles[i]) + "': " + str(self._valeurs[i]) + ", "
                i += 1
            affiche = affiche + "'" + str(self._cles[i]) + "': " + str(self._valeurs[i]) + "}"
        elif taille == 1:
            affiche = "{'" + str(self._cles[0]) + "': " + str(self._valeurs[0]) + "}"
        elif taille == 0:
            affiche = "{}"
        return affiche
    def __delitem__(self,cle):
        if cle in self._cles:
            indice = self._cles.index(cle)
            del self._valeurs[indice]
            del self._cles[indice]
        else:
            raise ValueError ("La cle à effacer n'est pas trouvée")
    def __contains__(self,cle):
        if cle in self._cles:
            return True
        else:
            return False
    def __len__(self):
        return len(self._cles)
    def __str__(self):
        return repr(self)
    def __iter__(self):
        """Retourne un iterateur d'un objet liste""" 
        return itSortDict(self._cles)
    def __add__(self, objetAjouter):
        for i, cle in enumerate(objetAjouter):
            self._cles.append(cle)
            self._valeurs.append(objetAjouter._valeurs[i])
        return self
    def sort(self):
        nonSortValeurs = list()
        nonSortCles = self._cles
        for val in self._valeurs:
            nonSortValeurs.append(val)
        sortCles = sorted(self._cles)
        self._cles = sortCles
        for nonCleEle in nonSortCles:
            indice = nonSortCles.index(nonCleEle)
            for sortCleEle in sortCles:
                indiceFin = sortCles.index(sortCleEle)
                if sortCleEle == nonCleEle:
                    self._valeurs[indiceFin] = nonSortValeurs[indice]
    def reverse(self):
        nonSortValeurs = list()
        nonSortCles = self._cles
        for val in self._valeurs:
            nonSortValeurs.append(val)
        sortCles = sorted(self._cles, reverse=True)
        self._cles = sortCles
        for nonCleEle in nonSortCles:
            indice = nonSortCles.index(nonCleEle)
            for sortCleEle in sortCles:
                indiceFin = sortCles.index(sortCleEle)
                if sortCleEle == nonCleEle:
                    self._valeurs[indiceFin] = nonSortValeurs[indice]
    def keys(self):
        return list(self._cles)
    def values(self):
        return list(self._valeurs)
    def items(self):
        for i, cle in enumerate(self._cles):
            valeurs = self._valeurs[i]
            yield (cle, valeurs)

class itSortDict:
    """Iterateur avec son constructeur 
            - liste a parcourir
            - position de l'objet courant"""
    def __init__(self, listeAParcourir):
        self.listeAParcourir = listeAParcourir
        self.position = -1
    def __next__(self):
        if self.position == (len(self.listeAParcourir) - 1):
            raise StopIteration
        self.position += 1
        return self.listeAParcourir[self.position]

foo = SortDict(pommes=3, abricots=32, oeufs=1, batate=42)
foo1 = SortDict(melons=44, mijote=2)
foo.sort()
print(foo)
foo.reverse()
print(foo)


for cle in foo:
    print(cle)

b = foo.keys()
a = foo.values()
for it in a:
    print(it)
for it in b:
    print(it)

ff = foo.items()
print(ff)

for cle in ff:
    print(cle)

foo2 = foo1 + foo

print(foo2)


fruits = SortDict()
fruits
fruits["pomme"] = 52
fruits["poire"] = 34
fruits["prune"] = 128
fruits["melon"] = 15
fruits
#{'pomme': 52, 'poire': 34, 'prune': 128, 'melon': 15}
fruits.sort()
print(fruits)
#{'melon': 15, 'poire': 34, 'pomme': 52, 'prune': 128}
legumes = SortDict(carotte = 26, haricot = 48)
print(legumes)
#{'carotte': 26, 'haricot': 48}
len(legumes)
#2
legumes.reverse()
fruits = fruits + legumes
fruits
#{'melon': 15, 'poire': 34, 'pomme': 52, 'prune': 128, 'haricot': 48, 'carotte':
#26}
del fruits['haricot']
'haricot' in fruits
#False
legumes['haricot']
#48
for cle in legumes:
    print(cle)
#haricot
#carotte
legumes.keys()
#['haricot', 'carotte']
legumes.values()
#[48, 26]
for nom, qtt in legumes.items():
    print("{0} ({1})".format(nom, qtt))

#haricot (48)
#carotte (26)