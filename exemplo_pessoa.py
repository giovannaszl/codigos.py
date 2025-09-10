from exemplo_carro2 import Carro # Importando a classe carro

class pessoa:

    def __init__(self, nome, idade, cidade, exemplo_carro2: Carro):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.exemplo_carro2 = Carro

    def apresentar(self):
        print(f"A pessoa {self.nome}, {self.idade}, {self.cidade} está se apresentando!")
    def dirigir(self):
        print(f"Olá meu nome é {self.nome} tenho {self.idade} moro na cidade {self.cidade}"):
        self.exemplo_carro2.acelerar()

# Criando pessoas diferentes
pessoa1 = pessoa("Gael", "15 anos", "Curitiba")
pessoa2 = pessoa("Carolina", "19 anos", "São Paulo")
pessoa3 = pessoa("Giovanna", "13 anos", "Salvador")
pessoa4 = pessoa("Oliver", "3 anos", "São Paulo")

# Chamando meteodos
pessoa1.apresentar()  # Usar os atributos da pessoa1
pessoa2.apresentar()  # Usar os atributos da pessoa2
pessoa3.apresentar()
pessoa4.apresentar() 