class Usuario:
    cargo = 'usuario'

    def __init__(self, nome, idade, altura):
        self.altura = altura

    def retorna_Altura(self):
        print(self.altura)

    def exibe_cargo(cls):
        print(cls.cargo)

usuario1 = Usuario('Digas', '17', '173')
usuario2 = Usuario('Vitor', '19', '180')

Usuario.cargo = 'Gerente'


usuario1.exibe_cargo()
usuario2.exibe_cargo()