m = [[None for _ in range(3)] for _ in range(5)]
i = 0


for l in range(0, len(m)):
    for c in range(0, len(m[l])):
        m[l][c] = i
        i += 1
        
        
print(m)