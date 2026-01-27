# Crie uma classe Aluno com atributos nome e nota.
# Depois crie uma classe Turma que tenha uma lista de alunos
# e um método adicionar_aluno(aluno). Crie alguns objetos
# Aluno e adicione-os à turma.


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


class Turma:
    def __init__(self):
        self.lista = []

    def adicionar_aluno(self, aluno):
        self.lista.append(aluno)


aluno1 = Aluno("Maria", 8)
aluno2 = Aluno("João", 10)
aluno3 = Aluno("Felipe", 7)

turm = Turma()
turm.adicionar_aluno(aluno1)
turm.adicionar_aluno(aluno2)
turm.adicionar_aluno(aluno3)

print(turm.lista)
