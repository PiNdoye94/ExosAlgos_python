a = int(input("saisir une valeur de a: "))
b = int(input("saisir une valeur de b: "))
quotient = int(0)
if (a>b):
   while (a>=b):
       a = a-b
       quotient = quotient+1
else:
    while (a<=b):
         b = b-a
         quotient = quotient+1
print("le quotient de la division par soustraction est: ",quotient)   
    
