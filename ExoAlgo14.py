print("saisir une date pour voir si l'année est bissextile:")
jour = int(input("entrer jour: "))
mois = int(input("entrer mois: "))
annee = int(input("entrer annee: "))
print("Date:",jour,"/",mois,"/",annee)
if (annee%4==0 and annee%100!=0 or annee%400==0):
    print("l'annee est bissextile.")
else:
    print("l'annee n'est pas bissextile!")
