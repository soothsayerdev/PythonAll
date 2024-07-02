def junta(arquivo1, arquivo2, resultado):
    with open(arquivo1, 'r') as file1, open(arquivo2, 'r') as file2:
        conteudo1 = file1.readlines()
        conteudo2 = file2.readlines()
    
    linhas_unicas = sorted(set(conteudo1 + conteudo2))
    
    with open(resultado, 'w') as file_result:
        file_result.writelines(linhas_unicas)

# Exemplo de uso
arquivo1 = 'arquivo1.txt'
arquivo2 = 'arquivo2.txt'
resultado = 'arquivo3.txt'
junta(arquivo1, arquivo2, resultado)
