# -*-coding:Latin-1 -*
#import random
#import sys
#import time

## Répète 20 fois
#i = 0
#while i < 20:
#    sys.stdout.write("1")
#    sys.stdout.flush()
#    attente = 0.2
#    attente += random.randint(1, 60) / 100
#    # attente est à présent entre 0.2 et 0.8
#    i += 1
from threading import Thread, RLock
import random
import sys
import time


verrou = RLock()

class Afficheur(Thread):
    def __init__(self, lettre):
        """Thread chargé simplement d'afficher une lettre dans la console"""
        Thread.__init__(self)
        self.lettre = lettre
    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            # attente est à présent entre 0.2 et 0.8
            i += 1

class AfficheurMots(Thread):
    def __init__(self, mot):
        """Thread chargé simplement d'afficher un mot dans la console"""
        Thread.__init__(self)
        self.mot = mot
    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        time.sleep(0.5)
        while i < 5:
            with verrou:
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            i += 1
        

#Création des threads
thread1 = Afficheur("1")
thread2 = Afficheur("2")
thread3 = Afficheur("3")
thread4 = AfficheurMots("CARACOLA")
thread5 = AfficheurMots("sibim")
thread6 = AfficheurMots("123123")

#Lancement des threads  
thread4.start()
thread5.start()
thread6.start()

# Attend que les threads se terminent
thread4.join()
thread5.join()
thread6.join()