# Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.

class Onibus:
    def __init__(self, numero, motorista):
        self.numero = numero
        self.motorista = motorista

    def transportar(self, aluno_nome):
        print(f"O ônibus {self.numero}, dirigido por {self.motorista}, está levando {aluno_nome} para a escola.")

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def ir_para_escola(self, onibus):
        print(f"{self.nome} vai para a escola.")
        onibus.transportar(self.nome)

onibus_escolar = Onibus("B12","Sr. João")
aluno1 = Aluno("Carlos")

aluno1.ir_para_escola(onibus_escolar)




 
