# Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos
# (por exemplo, mudar o ano). Imprima antes e depois da alteração.


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def apresentar(self):
        print(f"\nMarca: {self.marca} Modelo: {self.modelo} Ano: {self.ano}.")


carro1 = Carro("Toyota", "Corolla", 2020)

print("\nAntes da alteração:")

carro1.apresentar()

print("\nDepois da alteração:")

carro1.ano = 2025

carro1.apresentar()
