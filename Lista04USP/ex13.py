import math

class Fracao:
    def __init__(self, numerador=0, denominador=1):
        self.numerador = numerador
        self.denominador = denominador
        self.reduz()
    
    def mdc(self, a, b):
        return math.gcd(a, b)
    
    def reduz(self):
        divisor_comum = self.mdc(self.numerador, self.denominador)
        self.numerador //= divisor_comum
        self.denominador //= divisor_comum
        if self.denominador < 0:
            self.numerador = -self.numerador
            self.denominador = -self.denominador

    def add(self, b):
        novo_numerador = self.numerador * b.denominador + b.numerador * self.denominador
        novo_denominador = self.denominador * b.denominador
        return Fracao(novo_numerador, novo_denominador)

    def sub(self, b):
        novo_numerador = self.numerador * b.denominador - b.numerador * self.denominador
        novo_denominador = self.denominador * b.denominador
        return Fracao(novo_numerador, novo_denominador)

    def mul(self, b):
        novo_numerador = self.numerador * b.numerador
        novo_denominador = self.denominador * b.denominador
        return Fracao(novo_numerador, novo_denominador)

    def truediv(self, b):
        novo_numerador = self.numerador * b.denominador
        novo_denominador = self.denominador * b.numerador
        return Fracao(novo_numerador, novo_denominador)

    def floordiv(self, b):
        return self.numerador // self.denominador // (b.numerador // b.denominador)

    def float(self):
        return self.numerador / self.denominador

    def __str__(self):
        if self.denominador == 1:
            return str(self.numerador)
        else:
            return f'{self.numerador}/{self.denominador}'

# Exemplos de uso
f = Fracao()
print(f, float(f))  # Deve imprimir 0 0.0

f = f.add(Fracao(1, 2))
print(f, float(f))  # Deve imprimir 1/2 0.5

f = f.add(Fracao(1, 2))
print(f, float(f))  # Deve imprimir 1 1.0

f = f.mul(Fracao(3, 2))
print(f, float(f))  # Deve imprimir 3/2 1.5

f = f.truediv(Fracao(3, 4))
print(f, float(f))  # Deve imprimir 2 2.0

f = f.sub(Fracao(1, 6))
print(f, float(f))  # Deve imprimir 11/6 1.8333333333333333

f = f.mul(Fracao(0, 99999999999999))
print(f, float(f))  # Deve imprimir 0 0.0
