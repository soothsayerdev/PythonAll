import ast

def interpreta(string):
    try:
        # Tentar converter a string usando ast.literal_eval
        result = ast.literal_eval(string)
    except (ValueError, SyntaxError):
        # Se der erro, lançar exceção com mensagem "Tipo Desconhecido"
        raise Exception("Tipo Desconhecido")
    
    # Verificar se o resultado é de um dos tipos permitidos
    if isinstance(result, (str, bytes, int, float, complex, list, tuple, dict, set, bool, type(None))):
        return result
    else:
        # Se não for, lançar exceção com mensagem "Tipo Desconhecido"
        raise Exception("Tipo Desconhecido")

# Exemplos de uso
try:
    print(interpreta('teste'))
except Exception as e:
    print(e)

try:
    print(interpreta('[1,2,{1:2}]'))
except Exception as e:
    print(e)
