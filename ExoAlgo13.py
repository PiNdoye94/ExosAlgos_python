print("définir une date au format jj/mm/aa pour voir si elle est valide ou pas: ")
jour = int(input("entrer le jour la date: "))
mois = int(input("entrer le mois de la date: "))
annee = int(input("entrer l'année de cette date: "))
if (annee>=2020):
    if (jour>0 and jour<31):
        if (mois>0 and mois<12):
            print("la date",jour,"/",mois,"/",annee," est valide.")
else:
    print("la date saisie est invalide!")
