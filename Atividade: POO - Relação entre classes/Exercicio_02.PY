class Onibus:
    def __init__(self, linha, empresa):
        self.linha = linha
        self.empresa = empresa

    def iniciar_trajeto(self):
        return f"Linha {self.linha} saindo em direção à Universidade..."

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    # Este método demonstra a associação/dependência
    def ir_para_escola(self, onibus_escolhido):
        print(f"O aluno {self.nome} (Matrícula: {self.matricula}) entrou no ônibus.")
        print(onibus_escolhido.iniciar_trajeto())