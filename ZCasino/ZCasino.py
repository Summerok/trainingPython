# -*-coding:Latin-1 -*

import random
import math
import os
import sys 

solde = 1000
continuer_jeu = 1

def croupier(valeur_mise, valeur_essai, montant):
#Cette fonction réalise le calcul que le croupier effectue
        print ("La valeur de la roulette est : ", valeur_essai)
        if valeur_essai == valeur_mise:
                print ("Vous avez gagné avec votre mise. Recevez 3 fois votre mise :", montant * 3)
                return montant * 3
        elif valeur_essai % 2 == 0 and valeur_mise % 2 == 0:
                print ("Vous avez misé sur la coleur noire, comme l'essai. Recevez la moitié de votre mise :", math.ceil(montant * 0.5))
                return math.ceil(montant * 0.5)
        elif valeur_essai % 2 == 1 and valeur_mise % 2 == 1:
                print ("Vous avez misé sur la coleur rouge, comme l'essai. Recevez la moitié de votre mise :", math.ceil(montant * 0.5))
                return math.ceil(montant * 0.5)
        else:
                print ("Votre mise n'est pas gagnante. Désolé, votre mise est perdue.")
                return 0
print ("Prenez votre place pour jouer au jeu de la roulette avec", solde, "$.")

while continuer_jeu == 1:
        num_mise = -1
        while num_mise < 0 or num_mise > 49:
                try:
                        num_mise = int(input("Insérez le numéro sur lequel vous misez : \n"))
                except ValueError:
                        print ("Vous n'avez pas inséré un numéro entre 0 et 49")
                except NameError:
                        print ("Vous n'avez pas inséré un numéro. Insérez un numéro entre 0 et 49")
                except SyntaxError:
                        print ("Vous n'avez pas inséré un numéro. Insérez un numéro entre 0 et 49")

        montant_mise = 0
        while montant_mise <= 0 or montant_mise > solde:
                try:
                        montant_mise = int(input("Insérez le montant de la mise : \n"))
                except ValueError:
                        print ("Vous n'avez pas inséré une mise cohérente")
                        montant_mise = -1
                except NameError:
                        print ("Insérez un numéro pour la mise")
                        montant_mise = -1
        solde = solde - montant_mise
        print ("La roulette est en train de tourner...")
        num_rand = random.randrange(50)
        solde = solde + croupier(num_mise, num_rand, montant_mise)

        if solde <= 0:
                print ("Vous êtes sans argent, vous devez quitter le jeu")
                continuer_jeu = 0
        else:
                print ("Votre solde restant est de ", solde, "$")
                sortir = input("Est-ce que vous voulez sortir du jeu (o/n) ?\n")
                if sortir == "o" or sortir == "O":
                        continuer_jeu = 0
                        print ("Au revoir ! N'oubliez pas vos", solde, "$ avant de partir")
os.system("pause")
