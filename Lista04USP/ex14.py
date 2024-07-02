import math

class Vetor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def add(self, b):
        return Vetor(self.x + b.x, self.y + b.y)
    
    def sub(self, b):
        return Vetor(self.x - b.x, self.y - b.y)
    
    def mul(self, b):
        return self.x * b.x + self.y * b.y
    
    def xor(self, b):
        return self.x * b.y - self.y * b.x
    
    def abs(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __str__(self):
        return f'({self.x}, {self.y})'

# Exemplos de uso
v = Vetor()
print(v)  # Deve imprimir (0, 0)

v = v.add(Vetor(1, 2))
print(v)  # Deve imprimir (1, 2)

v = v.add(Vetor(1, 2))
print(v)  # Deve imprimir (2, 4)

v = v.sub(Vetor(1, 6))
print(v)  # Deve imprimir (1, -2)

a = v.mul(Vetor(3, 2))
print(a)  # Deve imprimir 7

b = v.xor(Vetor(-4501, 9002))
print(b)  # Deve imprimir -18010

c = v.abs()
print(c)  # Deve imprimir aproximadamente 2.23606797749979
