import re
import string

def info(arquivo):
    with open(arquivo, 'r') as file:
        conteudo = file.read()  # Lê todo o conteúdo do arquivo
    
    num_linhas = len(conteudo.splitlines())
    
    vogais = re.findall(r'[aeiouAEIOU]', conteudo)
    consoantes = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', conteudo)
    digitos = re.findall(r'\d', conteudo)
    sinais_pontuacao = re.findall(r'[{}]'.format(re.escape(string.punctuation)), conteudo)
    espacos_brancos = re.findall(r'[ \t]', conteudo)
    
    return (num_linhas, len(vogais), len(consoantes), len(digitos), len(sinais_pontuacao), len(espacos_brancos))

# Exemplo de uso
nome_arquivo = 'arquivo.txt'
resultado = info(nome_arquivo)
print(resultado)
