print("entrer l'heure de départ")
heuredep = int(input("heure: "))
mindep = int(input("minutes: "))
print("entrer l'heure d'arrivée")
heuredav = int(input("heure: "))
mindav = int(input("minutes: "))
if (mindav>mindep):
    duremin = mindav-mindep
    dureheure = 24-heuredep+heuredav
    print("la duréée du vol est de ",dureheure,"h-",duremin,"mns")
else:
    duremin = mindav+60-mindep
    dureheure = 24-heuredep+heuredav
    print("la duréée du vol est de ",dureheure,"h -",duremin,"mns")
