class Carro:
   
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"O carro {self.marca} {self.modelo} está acelerando!")


# Criando dois objetos diferentes
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")
carro3 = Carro("Volkswagen", "Golf")

# Chamando métodos
carro1.acelerar()  # Usa os atributos do carro1
carro2.acelerar()  # Usa os atributos do carro2
carro3.acelerar()  

