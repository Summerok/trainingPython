
try:
        annee = input("Insérez l'année\n")
        annee = int(annee)
except:
	print ("you should insert a number")
	
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0) :
	print "l'année saisie est bissextile"
else :
	print "l'année saisie n'est pas bissextile"
