from collections import deque

class Fila:
    def __init__(self): 
        self.fila = deque()
        
    
    def enfileirar(self, elemento):
        self.fila.append(elemento)
        
    def desenfileirar(self):
        if not self.esta_vazia():
            return self.fila.popleft()
        else:
            return "Fila vazia!"
        
    
    def esta_vazia(self):
        return len(self.fila) == 0
    
    
    def tamanho(self):
        return len(self.fila)
    
    def primeiro(self):
        if not self.esta_vazia():
            return self.fila[0]
        else:
            return "Fila vazia!"
        

def triggerSW(a, fp, x, y):
    for i in a:
        if i == y:
            fp.enfileirar(i)  
        fp.enfileirar(i)  
    
    

# Exemplo de uso:
a = ["x", "x", "y", "x"]
x, y = "x", "y"

# Inicializa a fila
fp = Fila()

triggerSW(a, fp, x, y)

print(list(fp.fila))