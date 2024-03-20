m = [
        [0, 1, 2], 
        [2, 3, 3],
        [4, 5],
        [6, 7]
    ]

vpares = []

for l in range(0, len(m)):
    for c in range(0, len(m[l])):
        if m[l][c] % 2 == 0:
            vpares.append(m[l][c])
        
            
        
print(" ")
print(vpares)