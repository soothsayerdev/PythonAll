def primo():
    n = int(input(""))
    c = 0
    
    if n != 2 or n != 3:
        if n % 2 == 0:
            c += 1
        
        if n % 3 == 0:
            c += 1    
   
    if n % n == 0:
        c += 1
        
    if c > 1:
        print("Não primo")
    
    elif c<= 1:
        print("Primo")

primo()