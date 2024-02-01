class Pessoa:
    def __init__(self, nome, cpf, altura):
        self.cpf = cpf
        self.altura = altura
        self.nome = nome
        


class Secretaria(Pessoa):
    def __init__(self, id_secretaria, nome, cpf, altura):
        super().__init__(nome, cpf,  altura)
        self.id_secretaria = id_secretaria
        
class Vendedor(Pessoa):
    pass

s1 = Secretaria('2','Digas', '3928428904', '178')
v1 = Vendedor('Vitor', '20492140', '167')

