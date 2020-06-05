n = int(input("saisir n pour calculer la somme des entiers jusqu'à ce nombre et sa moyenne: "))
somme = int(0)
for i in range(1,n+1):
    somme = somme+i
moyenne = somme/n
print("la somme des valeurs inferieurs de n est: ", somme)
print("la moyenne est: ", moyenne)
