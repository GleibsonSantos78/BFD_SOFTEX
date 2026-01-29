class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __str__(self):
        return f"{self.nome} ({self.posicao})"

class Time:
    def __init__(self, nome_time):
        self.nome_time = nome_time
        self.elenco = []  # Lista que receberá os objetos Jogador

    def contratar_jogador(self, jogador):
        self.elenco.append(jogador)
        print(f"O jogador {jogador.nome} foi inscrito no {self.nome_time}!")

    def exibir_escalacao(self):
        print(f"\n--- Escalação: {self.nome_time} ---")
        if not self.elenco:
            print("Time sem jogadores no momento.")
        else:
            for jogador in self.elenco:
                print(f"• {jogador}")