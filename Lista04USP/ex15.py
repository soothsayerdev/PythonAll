import math
import random

class Polinomio2:
    def __init__(self, a=None, b=None, c=None):
        if a is None:
            a = random.randint(-10, 10)
        if b is None:
            b = random.randint(-10, 10)
        if c is None:
            c = random.randint(-10, 10)
        self.a = a
        self.b = b
        self.c = c
    
    def raizes(self):
        delta = self.b ** 2 - 4 * self.a * self.c
        if delta < 0:
            return []
        elif delta == 0:
            return [-self.b / (2 * self.a)]
        else:
            x1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            return [x1, x2]
    
    def valor(self, x):
        return self.a * x ** 2 + self.b * x + self.c

def coeficientes(polinomio):
    a = polinomio.valor(1) - polinomio.valor(0)
    b = polinomio.valor(0)
    c = polinomio.valor(-1)
    return a, b, c

# Exemplos de uso
p1 = Polinomio2(1, 1, 1)
print(p1.raizes())  # Deve imprimir []

print(p1.valor(2))  # Deve imprimir 7

p2 = Polinomio2(1, 2, 1)
print(p2.raizes())  # Deve imprimir [-1.0]

print(p2.valor(2))  # Deve imprimir 9

p3 = Polinomio2(1, -3, 2)
print(p3.raizes())  # Deve imprimir [2.0, 1.0]

print(p3.valor(2))  # Deve imprimir 0
