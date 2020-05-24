R1 = int(input("saisir la valeur de la resistance R1: "))
R2 = int(input("entrer la valeur de la resistance R2: "))
R3 = int(input("entrer la valeur de la resistance R3: "))
choix = int(input("entrer votre choix qui ne peut etre que deux valeurs 1 ou 2!: "))
if (choix==1):
    RT = R1+R2+R3
    print("la resistance totale du circuit en série est: ", RT," ohm")
elif (choix==2):
    RT = (R1*R2*R3)/(R1*R2+R2*R3+R1*R3)
    print("la resistance totale du circuit en parallele est: ", RT," ohm")
else:
    print("choix impossible!!")
