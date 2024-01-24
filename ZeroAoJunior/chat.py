import os 

mensagens = []

nome = input('Nome: ')

while True:
    
    # limpando terminal
    os.system('cls')
    
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])
    
    print('__________________________')
    
    #obtendo texto
    texto = input('mensagem: ')
    if texto == 'fim':
        break
            