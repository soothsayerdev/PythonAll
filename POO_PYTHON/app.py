class Usuario:
#    cargo = 'usuario'

    def __init__(self, nome, idade, altura):
        self.altura = altura

    @classmethod    # Possibilita acessar diretamente pela classe
    def retorna_Altura(self):
        print(self.altura)

    #@classmethod
    @staticmethod # Mantem travado/estatico a funcao
#    def exibe_cargo(cls):
        # cls.cargo = "Gerente"
#        print(cls.cargo)

    @classmethod
    def teste(cls):
        return 1

    @staticmethod # Impede pegar e chamar outras instancias de fora da def na classe
    def e_adulto(idade):
        if idade >= 18:
            print(True)
        else: 
            print(False)


Usuario.e_adulto(17)



#usuario1 = Usuario('Digas', '17', '173')
#usuario2 = Usuario('Vitor', '19', '180')

#usuario1.exibe_cargo()
#usuario2.exibe_cargo()
        
Usuario.exibe_cargo()