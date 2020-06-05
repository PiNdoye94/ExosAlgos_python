n = int(input("saisir une valeur n: "))
somme = int(1)
if (n == 0):
    print("le nombre saisi n'est pas parfait!")
else:
    for i in range(2,n//2+1):        
        if (n%i==0):              
            somme = somme+i
    if (n==somme):            
        print("le nombre",n,"est parfait")
    else:            
        print("le nombre",n,"n'est pa parfait")
        


