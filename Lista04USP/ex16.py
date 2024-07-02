class Arquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.index = 0
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        with open(self.arquivo, 'r') as f:
            linhas = f.readlines()
            if self.index < len(linhas):
                linha = linhas[self.index]
                self.index += 1
                return linha.strip()
            else:
                raise StopIteration

a = Arquivo('arquivo.txt')
for linha in a:
    print(linha)
