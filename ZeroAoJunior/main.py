print("Quero meu primeiro emprego!")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(nome)
print(idade)
print(peso) 

soma = 1 + 1 
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2

print("Soma: ", soma)
print("Multiplicacao: ", multiplicacao)
print("Divisao: ", divisao)
print("Potencia: ", potencia)

if idade >= 18:
    print("PERMITIDO!")
else: 
    print("BLOQUEADO")


notas = []

print( "Quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("0 RM", codigo_aluno, "tirou a nota: ", nota)
    
    
salario = float(input("Informe seu salario: "))

if salario <= 3000:
    print("programador Junior")
elif salario > 3000 and salario <= 6000:
    print("programador Pleno")
elif salario > 6000 and salario <= 15000:
    print("programador Senior")
else: 
    print("Gerente de projetos")
    


    



    
    
    
    
    
    
    
    
    
    