x = [1,2,3,4,5,6,7,8,9,10]
fim = len(x) - 1
#y = []

#for i in range(len(x)-1, -1, -1):
#    y.append(x[i])

#print(y)

for i in range(len(x)//2):
    aux = x[i]
    x[i] = x[fim]
    x[fim] = aux
    fim -= 1

print(x)
