# Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). Cada Comodo deve ser criado dentro da Casa.

class Comodo:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Comodo: {self.nome}"
    
class Casa:
    def __init__(self):
        self.comodos = []

    def adicionar_comodo(self, comodo):
        self.comodos.append(comodo)

    def listar_comodos(self):
        for comodo in self.comodos:
            print(comodo)


casa = Casa()
sala = Comodo("Sala")
cozinha = Comodo("Cozinha")
quarto = Comodo("Quarto")
casa.adicionar_comodo(sala)
casa.adicionar_comodo(cozinha)
casa.adicionar_comodo(quarto)
casa.listar_comodos()


