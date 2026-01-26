# Crie uma classe Carro com os atributos marca,
# modelo e ano. Use o método __init__ para inicializar esses valores.
# Crie três objetos e mostre suas informações.


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def apresentar(self):
        print(f"\nMarca: {self.marca} Modelo: {self.modelo} Ano: {self.ano}.")


carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2022)
carro3 = Carro("Ford", "Mustang", 2023)

carro1.apresentar()
carro2.apresentar()
carro3.apresentar()
