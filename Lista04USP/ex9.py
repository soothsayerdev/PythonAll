def msb(n):
    if n == 0:
        return -1  # Caso especial: se n for 0, não há bits 1, então retornamos -1 ou outro valor que indique ausência de bit 1
    
    pos = 0
    while n > 0:
        n >>= 1  # Desloca n um bit para a direita
        pos += 1  # Incrementa a posição do bit
        
    return pos - 1  # Retorna a posição do último bit 1 encontrado

# Exemplos de uso
print(msb(5))  # Deve retornar 2 (o bit mais significativo de 5 é na posição 2)
print(msb(4))  # Deve retornar 2 (o bit mais significativo de 4 é na posição 2)
