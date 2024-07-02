def bit(x, n):
    return (x >> n) & 1

# Exemplos de uso
print(bit(5, 0))  # Deve retornar 1 (o bit na posição 0 de 5 é 1)
print(bit(5, 2))  # Deve retornar 1 (o bit na posição 2 de 5 é 1)
