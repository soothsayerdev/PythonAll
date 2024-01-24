# Metodo        Parametros          Resultado       Descricao   
# append        item                mutador         Acrescenta um novo item no final da lista
# insert        posicao,item        mutador         Insere um novo item na posicao dada
# pop           nenhum              hibrido         Remove e retorna o ultimo item
# pop           posicao             hibrido         Remove e retorna o item da posicao
# sort          nenhum              mutador         Ordena a lista
# reverse       nenhum              mutador         Ordena a lista em ordem reversa
# index         item                retorna idx     Retorna a posicao da primeira ocorrencia do item
# count         item                retorna ct      Retorna o numero de ocorrencias do item
# remove        item                mutador         Remopve a primeira ocorrencia do item

numeros = [10, 9, 8, 7, 6]

print( "Total: ", len(numeros) )
print( "Menor valor: ", min(numeros) )
print( "Maior valor: ", max(numeros) )





notas = []

for x in range(300):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    

contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    
    #alternativa: contador += 1
    contador = contador + 1
    
print( "quantidade de notas ", len(notas))

# Dicionarios

pessoa = {
    "nome": "Programador Python",
    "idade": 17,
    "peso": 50.2
}

print( pessoa['nome'] )
print( pessoa["idade"] )
print( pessoa["peso"] )

# informacoes do jogador

player = {
    "nome": "Digas",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano": 5,
    
}

# lista de inimigos

npcs = [
    { "nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5},
    { "nome": "Monstro", "dano": 5, "hp": 100, "exp": 10},
    { "nome": "Monstrao", "dano": 10, "hp": 150, "exp": 15},
    { "nome": "Chefao", "dano": 25, "hp": 200, "exp": 20},
    
]

# os.getcwd(): Obtem o diretorio de trabalho atual.
# os.listdir(path): Lista os arquivos e diretorios em um caminho especifico.
# os.path.join(path, *paths): Lista os arquivos e diretorios em um caminho expecifico.
# os.path.join(path, *paths): Combina partes de caminhos para formar um novo caminho
# os.path.exists(path): Verifica se um caminho existe
# os


numeros2 = [1,2,3]
strings = ["Joao", "Maria", "Bruxa"]
decimais = [10.8, 15.2, 33.3]

lista_vazia = []

lista_vazia.append("Ola")
lista_vazia.append("Mundo")

print(lista_vazia) 
#pedrolove
