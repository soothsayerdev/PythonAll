def zeros(n):
    count = 0
    
    # Enquanto n for diferente de 0 e o último bit for 0
    while n != 0 and n & 1 == 0:
        count += 1
        n >>= 1  # Desloca n um bit para a direita
    
    return count

# Exemplos de uso
print(zeros(5))  # Deve retornar 0 (número binário: 101)
print(zeros(4))  # Deve retornar 2 (número binário: 100)
