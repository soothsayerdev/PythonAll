class Televisao:
    def __init__(self, ligada=False, canal=1):
        self.ligada = ligada
        self.canal = canal
    
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def canal_cima(self):
        if self.ligada:
            self.canal = min(self.canal + 1, 100 if self.canal <= 99 else self.canal)
    
    def canal_baixo(self):
        if self.ligada:
            self.canal = max(self.canal - 1, 1 if self.canal >= 2 else self.canal)
    
    def __str__(self):
        return f'({self.ligada}, {self.canal})'

# Exemplos de uso
tv = Televisao()
print(tv)  # Deve imprimir (False, 1)

tv.canal_cima()
print(tv)  # Deve imprimir (False, 1)

tv.canal_baixo()
print(tv)  # Deve imprimir (False, 1)

tv.liga()
print(tv)  # Deve imprimir (True, 1)

tv.canal_cima()
print(tv)  # Deve imprimir (True, 2)

tv.canal_baixo()
print(tv)  # Deve imprimir (True, 1)

tv.desliga()
print(tv)  # Deve imprimir (False, 1)

tv.canal_cima()
print(tv)  # Deve imprimir (False, 1)
