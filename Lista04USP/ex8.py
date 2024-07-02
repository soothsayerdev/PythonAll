def troca(x, n):
    return x ^ (1 << n)

# Exemplos de uso
print(troca(5, 0))  # Deve retornar 4 (inverte o bit na posição 0 de 5)
print(troca(5, 2))  # Deve retornar 1 (inverte o bit na posição 2 de 5)
