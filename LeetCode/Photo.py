def verif_dimensao(x, y, l1, l2, h1, h2):
    
    entrada = [[x, y],
               [l1, h1],
               [l2, h2]
               ]
    
    if ((l1 > x or l2 > x) or (h1 > y or h2 > y)) == True:
        return "N"
    
    elif (x >= y and(l1 + l2 <= x) or (l1 + h2 <= x) or (l2 + h1 <= x)) == True:
        return "S"
    
    elif (y <= x and (h1 + h2 <= y) or (h1 + l2 <= y) or (h2 + l1 <= y)) == True:
        return "S"
    
    else:
        return "N"


x = 10
y = 10
l1, l2 = 6, 6
h1, h2 = 6, 6


print(verif_dimensao(x, y, l1, l2, h1, h2))
