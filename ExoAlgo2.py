import math
r = float(input("entrer le rayon du cercle: "))
s = r*r*4*math.atan(1)
p = 2*r*4*math.atan(1)
print("la surface du cercle est de ", s, "m2")
print("le perimetre du cercle est de: ", p, "m")
