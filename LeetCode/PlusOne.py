digits = [9]
aux = ""
nums = 0
resp = []

for i in digits:
    aux += str(i)
    
aux = int(aux)
aux += 1
aux = str(aux)

for i in aux:
    resp.append(i)
    
    
print(aux)
print(nums)
print(resp)