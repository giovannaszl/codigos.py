'''
O que é Polimorfismo?

É quando um mesmo méteodo tem comportamentos diferentes dependendo da classe que o usa.

Pense assim:

Todas as classe têm o méteodo apresentar(),

Mas cada classe fala de um jeito próprio quando você chama esse méteodo.
'''


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self): 
            print(f'olá, eu sou {self.nome}.')

class Cliente(Pessoa):
    def apresentar(self): # mesmo nome, mas comportamento diferente
        print(f"sou cliente {self.nome}, vim comprar algo.")

class Aluno(Pessoa):
    def apresentar(self): #Mesmo nome, mas comportamentos diferentes
        print(f"Sou aluno {self.nome}, estou estudando.")

#Criando objetos 
p= Pessoa('Carlos') 
c= Cliente('Maria')
a= Aluno('João')

# Chamando o MESMO méteodo "apresentar"
p.apresentar()
c.apresentar()
a.apresentar()