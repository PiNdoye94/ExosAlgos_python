print("entrer trois valeurs A, B et C pour les comparer: ")
A = int(input("saisir une valeur de A: "))
B = int(input("saisir une valeur de B: "))
C = int(input("saisir une valeur de C: "))

if A>B and A>C:
    if B>C:
        print("l'ordre croissant est: ",C, B, A)
    else:
        print("l'ordre croissant est: ",B, C, A)
elif B>A and B>C:
    if A>C:
        print("l'ordre croissant est: ",C, A, B)
    else:
        print("l'ordre croissant est: ",A, C, B)
elif C>A and C>B:
    if A>B:
        print("l'ordre croissant est: ",B, A, C)
    else:
        print("l'ordre croissant est: ",A, B, C)
