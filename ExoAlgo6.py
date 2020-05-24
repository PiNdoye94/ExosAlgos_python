from math import sqrt
print("coordonnées du point A(x1,y1)")
x1 = int(input("entrer l'abscisse du point A: "))
y1 = int(input("entrer l'ordonnée du point A: "))
print("coordonnées du point B(x2,y2)")
x2 = int(input("entrer l'abscisse du point B: "))
y2 = int(input("entrer l'ordonnée du point B: "))
D = sqrt((x1-x2)**2+(y1-y2)**2)
print("la distance entre les points A et B est: ", D,"m")
