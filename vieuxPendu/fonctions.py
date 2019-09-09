# -*-coding:Latin-1 -*
import random
import sys
import os
import pickle
from donnees import *

'''Fichier des fonctions utilisés par le jeu du vieux pendu'''
def choixMot(*liste):
    '''Objet: choisir au hasard un mot de la liste de mots pour le jeu'''
    rangDeMots = len(liste)
    i = random.randrange(rangDeMots)
    return liste[i]
	
def gestionLettre(mot, motDecStr, lettre):
    '''Objet: Gérer les lettres que le joueur insère dans le programme afin de trouver le mot'''
    i = 0
    numDec = 0
    motDecList = list(motDecStr)
    #while i < len(mot):
    for i,elt in enumerate(motDecList):
        if mot[i] == lettre:
            motDecList[i] = lettre
            numDec += 1
        else:
            pass    
    return numDec, "".join(motDecList)

def enregistrerScore(scores):
    '''Objet: Enregistrer le nom'''
    with open("scores", "wb") as fichier:
        monPickler = pickle.Pickler(fichier)
        monPickler.dump(scores)

def chargerScore():
    '''Objet: Charger les scores dans une variable de type dictionnaire'''
    try:
        with open("scores", "rb") as fichier:
            monDepickler = pickle.Unpickler(fichier)
            scoreRecupere = monDepickler.load()
        return scoreRecupere
    except FileNotFoundError:
        enregistrerScore(scores)

def montrerScore(score):
    print(*score)

def introduirUtilisateur():
    '''Objet: gestion de la correcte introduction du nom d'utilisateur'''
    nom_utilisateur = input("{}: Introduce tu nombre de usuaria\n".format(present))
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur) < 3:
        print("{}: El nombre de usuaria es inválido\n".format(present))
        return introduirUtilisateur()
    else: 
        return nom_utilisateur

def gestionEnter():
    '''Objet: gestion de l'introduction de la touche Entrée seulement'''
    enter = input("{}: Pulsa Enter cuando te sientas lista para empezar\n".format(present))
    if enter is not '':
        return gestionEnter()
    else:
        pass

def continuerJeu():
    '''Objet: gestion de la continuation du jeu'''
    cont = input("{}: Pulsa la tecla n para cerrar el juego\nPara continuar jugando pulsa la tecla Enter...".format(present)).lower()
    if cont != '' and cont != 'n':
        return continuerJeu()
    else:
        return cont

def recupLettre():
    '''Objet: gestion de l'introduction de la lettre'''
    rec_lettre = input("{}: Introduce una letra nueva\n".format(present)).lower()
    if len(rec_lettre) > 1 or not rec_lettre.isalpha():
        print("{}: No reconozco una letra en lo que has introducido".format(present))
        return recupLettre()
    else:
        return rec_lettre