#coding:utf-8
montant = int(input("saisir le montant souhaité: "))
billet20 = int(montant / 20)
reste = montant % 20
billet10 = int(reste / 10)
reste = reste % 10
billet5 = int(reste / 5)
reste = reste % 5
pièce2 = int(reste / 2)
reste = reste % 2
pièce1 = int(reste / 1)
reste = reste % 1

print("la décomposition du montant saisi est en billet de 20,10,5 euro et en pièce de 2,1 euro:\n", billet20,"\n",billet10,"\n",billet5,"\n",pièce2,"\n",pièce1)  
