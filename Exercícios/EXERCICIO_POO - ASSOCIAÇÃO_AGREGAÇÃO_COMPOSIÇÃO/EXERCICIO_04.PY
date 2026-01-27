# Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __str__(self):
        return f"{self.nome} - {self.posicao}"
class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        print(f"Time: {self.nome}")
        for jogador in self.jogadores:
            print(f" - {jogador}")

time1 = Time("Campeões FC")
jogador1 = Jogador("Ronaldo", "Atacante")
jogador2 = Jogador("Messi", "Meio-campo")
time1.adicionar_jogador(jogador1)
time1.adicionar_jogador(jogador2)
time1.listar_jogadores()


 
