a = int(input("saisir une valeur a: "))
opéra = str(input("saisir l'opérateur de calcul: "))
b = int(input("saisir une valeur b: "))
if opéra == "+":
    print("la somme de",a,"et",b,"est = ", a+b)
elif opéra == "-":
    print("la différence de",a,"et",b,"est =", a-b)
elif opéra == "*":
    print("la multiplication de",a,"et",b,"est =", a*b)
elif opéra == "/" and b!=0:
    print("la division de",a,"et",b,"est =", a/b)
else:
    print("Opération impossible!!")
