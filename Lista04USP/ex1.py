def inverte(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()  # Lê todas as linhas do arquivo
    
    linhas_invertidas = linhas[::-1]  # Inverte as linhas usando slicing

    with open(arquivo, 'w') as file:
        file.writelines(linhas_invertidas)  # Escreve as linhas invertidas de volta no arquivo

# Exemplo de uso
nome_arquivo = 'arquivo.txt'
inverte(nome_arquivo)

        