R1 = int(input("entrer la valeur de la resistance R1: "))
R2 = int(input("entrer la valeur de la resistance R2: "))
R3 = int(input("entrer la valeur de la resistance R3: "))
RT = R1 + R2 + R3
print("la résistance totale en circuit série est de: ", RT, "ohm")
RT = (R1*R2*R3)/(R1*R2 + R2*R3 + R1*R3)
print("la resistance totale en circuit parallele est de: ", RT, "ohm")
