vetor = [5,7,29,10,30,15]
inverseVet = vetor[-1]
print(inverseVet)

def separate():
    print("------------------------------------")

def soma_vetor():
    soma = 0

    for i in vetor:
        soma += i
            
    print(f"A soma dos indices no vetor é: {soma}")
    separate()

def maior_num():
    maior = 0
    if not vetor:
        print("Não posso avaliar um vetor vazio")
    
    for i in vetor:
        if i > maior:
            maior = i
    
    print(f"O maior valor do vetor é o numero: {maior}")
    separate()

def menor_num():
    menor = vetor[0]
    if not vetor:
        print("Não posso avaliar um vetor vazio")
    
    for i in vetor:
        if i < menor:
            menor = i

    print(f"O menor valor do vetor é o numero: {menor}")
    separate()

def media_arit():
    tam = len(vetor)
    soma2 = 0
    for i in vetor:
        soma2 += i

    media = soma2/tam
    print(f"A media aritmetica do vetor é: {media}")
    separate()

def qnts_pares():
    qt_pares = 0
    if not vetor:
        print("Não posso avaliar um vetor vazio")

    for i in vetor:
        if i % 2 == 0:
            qt_pares += 1
    print(f"A quantidade de numeros pares desse vetor é: {qt_pares}")
    separate()

def first_par():
    firstPar = 0
    for i in vetor:
        if i % 2 == 0:
            firstPar = i
            break
    print(f"O primeiro numero par do vetor é: {firstPar}")
    separate()

def last_par():
    lastPar = 0
    for i in reversed(vetor):
        if i % 2 == 0:
            lastPar = i
            break
    print(f"O ultimo numero par do vetor é: {lastPar}")

def indice_Fpar():
    indiceFpar = 0
    for i,j in enumerate(vetor):
        if j % 2 == 0:
            indiceFPar = i
            break
    print(f"O indice do primeiro par do vetor é {indiceFPar}")

def indice_Lpar():
    indiceLpar = 0
    for i,j in enumerate(reversed(vetor)):
        if j % 2 == 0:
            indiceLpar = i
            break
    print(f"O indice do ultimo par do vetor é: {indiceLpar}")

def pares_list():
    pares = []
    if not vetor:
        print("Não posso avaliar um vetor vazio")
    
    for i in vetor:
        if i % 2 == 0:
            pares.append(i)
    
    print(f"Os numeros pares do vetor são: {pares}")
    separate()


soma_vetor()
maior_num()
menor_num()
media_arit()
qnts_pares()
pares_list()
first_par()
indice_Fpar()
indice_Lpar()
last_par()