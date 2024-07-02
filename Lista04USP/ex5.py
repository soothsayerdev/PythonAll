import json

def is_json(string):
    try:
        # Tentar decodificar a string usando json.loads
        json.loads(string)
    except ValueError:
        # Se ocorrer um ValueError, a string não é um JSON válido
        return False
    return True

# Exemplos de uso
print(is_json('"teste"'))  # Deve retornar True
print(is_json('{1: 2}'))   # Deve retornar False
