# -*-coding:Latin-1 -*
from fonctions import *
from donnees import *


continueJeu = ''
#D�but du jeu
print("=====================================")
print("EL AHORCADO : Cr�nica de 1792")
print("=====================================")
print("")
nomJoueur = introduirUtilisateur()

if chargerScore() == None:
    scores[nomJoueur] = 0
    print("{}: Hola {}, �es tu primera vez? No te hab�a visto por aqu�.\nBienvenida a este fascinante juego, toma asiento y a jugar!".format(present, nomJoueur))
else:
    scores = chargerScore()
    try:
        scores[nomJoueur]
        print("{}: Hola {}, �qu� hay de nuevo?\nGuardas una puntuaci�n de {}. �A jugar!".format(present, nomJoueur, scores[nomJoueur]))
    except KeyError:
        scores[nomJoueur] = 0
        print("{}: Hola {}, �es tu primera vez? No te hab�a visto por aqu�.\nBienvenida a este fascinante juego, toma asiento y a jugar!".format(present, nomJoueur))

gestionEnter()

while continueJeu == '':
    motCherche = choixMot(*listeMots).lower()
    scr = len(motCherche)
    nLet = 0
    motDecStr = len(motCherche)*"*"
    mDecStr = ""
    print("{}: La palabra en juego tiene {} letras".format(present, scr))
    while scr > 0 and nLet < len(motCherche):
        nDec = 0
        lettre = recupLettre()
        nDec, mDecStr = gestionLettre(motCherche, motDecStr, lettre)
        if motDecStr.find(lettre) >= 0:
            print("{}: Esta letra ya la has descubierto!".format(present))
            continue
        if nDec > 0:
            print("{}: Has descubierto {} letras\n->>{}".format(present, nDec, mDecStr))
        else:
            scr -= 1
            print("{}: Lo siento, te quedan {} intentos".format(present, scr))
        nLet += nDec
        motDecStr = mDecStr
    if scr == 0:
        print("=====================================")
        print("GAME OVER")
        print("=====================================")
        print("{}: La palabra era {}".format(present, motCherche))

    else:
        print("=====================================")
        print("�ENHORABUENA! Encontraste la palabra")
        print("=====================================")

    print("{}: {}, tu puntuaci�n es de {}\nTu puntuaci�n total es de {}".format(present, nomJoueur, scr, scores[nomJoueur]+scr))
    continueJeu = continuerJeu()
    scores[nomJoueur] += scr 
    enregistrerScore(scores)
print("{}: Que tengas un buen d�a {}. Hasta pronto".format(present, nomJoueur))