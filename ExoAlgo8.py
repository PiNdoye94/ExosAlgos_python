from math import sqrt
print("entrer les coefficients a,b et c de l'équation: ")
a = int(input("saisir le coefficient directeur a: "))
b = int(input("saisir le coefficient b: "))
c = int(input("saisir le coefficient c: "))
D = int((b*b)-(4*a*c))
if (a==0):
    if (b==0):
        print("l'équation n'admet pas de solution!")
    else:
        print("la solution de l'équation est x= ",int(-c/b))
elif (D==0):
    print("l'équation admet une solution unique x0= ",int(-b/2*a))
elif ( D>0):
    print("l'équation admet une double solution x1= ",int(-b-sqrt(D)/2*a)," et x2= ",int(-b+sqrt(D))/2*a)
else:
    print("pas de solution possible!!")
