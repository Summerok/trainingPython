
try:
        annee = input("Ins�rez l'ann�e\n")
        annee = int(annee)
except:
	print ("you should insert a number")
	
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0) :
	print "l'ann�e saisie est bissextile"
else :
	print "l'ann�e saisie n'est pas bissextile"
