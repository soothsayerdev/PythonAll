pessoas = []
pessoasC = []
nPessoas = int(input("Digite quantas pessoas serão adicionadas a lista: "))
maiorP = []
menorP = []

def addPessoas():
    for i in range(0, nPessoas ):
        pessoasC.append(str(input("Nome: ")))
        pessoasC.append(float(input("Peso: ")))
        pessoas.append(pessoasC[:])
        pessoasC.clear()

def contagemPessoas():    
    print(f"O número de pessoas cadastradas foi {len(pessoas)}")
    
def listaPeso():
    for i in pessoas:
        if i[1] > 50:
            maiorP.append(i[0])
        
        elif i[1] < 50:
            menorP.append(i[0])
    
    print(f"As pessoas mais pesadas da lista são {maiorP}, e as pessoas mais leves são {menorP}")
    
    
addPessoas()
contagemPessoas()
listaPeso()