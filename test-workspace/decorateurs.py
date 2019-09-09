# -*-coding:Latin-1 -*
"""module multipli contenant la fonction table"""
import time


def compteurTemps(nbTemps):
    '''C'est le niveau qui prend le paramètre'''
    def decorateur(fonctionAExecuter):
        '''C'est le decorateur qui prend la fonction qu'on execute'''
        def fonctionAChanger(*parammetersNonNommes, **parammetersNommes):
            print("etape2")
            tempsAvant = time.time()
            fonctionAExecuter(*parammetersNonNommes, **parammetersNommes)
            print("etape3")
            tempsApres = time.time()
            tempsFonction = tempsApres - tempsAvant
            if tempsFonction > nbTemps:
                print("La fonction {0} met {1} d'exécution".format(fonctionAExecuter, tempsFonction))
        return fonctionAChanger
    return decorateur

@compteurTemps(2.5)
def attendre():
    print("etape1")
    input("Appuyez sur la touche Entrée...")

while 1:
    attendre()

attendre = compteurTemps(2.5)(attendre)