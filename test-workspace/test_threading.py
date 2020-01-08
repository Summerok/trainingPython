# -*-coding:Latin-1 -*
#import random
#import sys
#import time

## R�p�te 20 fois
#i = 0
#while i < 20:
#    sys.stdout.write("1")
#    sys.stdout.flush()
#    attente = 0.2
#    attente += random.randint(1, 60) / 100
#    # attente est � pr�sent entre 0.2 et 0.8
#    i += 1
import threading
import random
import sys
import time

class Afficheur(threading.Thread):
    def __init__(self, lettre):
        """Thread charg� simplement d'afficher une lettre dans la console"""
        threading.Thread.__init__(self)
        self.lettre = lettre
    def run(self):
        """Code � ex�cuter pendant l'ex�cution du thread."""
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            # attente est � pr�sent entre 0.2 et 0.8
            i += 1

#Cr�ation des threads
thread1 = Afficheur("1")
thread2 = Afficheur("2")
thread3 = Afficheur("3")

#Lancement des threads  
thread1.start()
thread2.start()
thread3.start()

# Attend que les threads se terminent
thread1.join()
thread2.join()
thread3.join()