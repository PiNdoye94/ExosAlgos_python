a = int(input("entrer une valeur a: "))
b = int(input("entrer une valeur b: "))
pgdc = int(0)
while(a%b!=0 or b%a!=0):
    if(a>b):
        pgdc = a//b
    else:
        pgdc = b//a
print("le pgcd entre a et b est: ", pgdc)         
