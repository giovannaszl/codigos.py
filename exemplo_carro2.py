class carro:

    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

        def acelerar(self):
            print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} está acelerando!.")

        def frear(self):
            print(f"O carro {self.marca} {self.modelo} {self.cor} {self.ano} está freando!.")

        # Criando dois objetos diferentes
        carro1 = carro("Jeep", "Renegade", "Prata", "2019")
        carro2 = carro("Audi", "A4", "Branco", "2020")
        carro3 = carro("Ferrari", "Roma", "Azul", "2021")

        # Chamando métodos
        carro1.acelerar()  # Usa os atributos do carro1
        carro1.frear()  # Usa os atributos do carro1
        carro2.acelerar()  # Usa os atributos do carro2
        carro2.frear()  #Usa os atributos do carro2
        carro3.acelerar()  
        carro3.frear()