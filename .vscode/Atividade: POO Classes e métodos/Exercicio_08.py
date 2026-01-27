# Na classe Aluno, implemente o método __str__ para que,
#  ao imprimir um objeto da classe, apareça algo como:"Aluno:
# Maria - Nota: 9.5". Teste imprimindo os objetos.


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome} - nota: {self.nota}"


class Turma:
    def __init__(self):
        self.lista = []

    def adicionar_aluno(self, aluno):
        self.lista.append(aluno)


aluno1 = Aluno("Maria", 9.5)

turm = Turma()
turm.adicionar_aluno(aluno1)


print(aluno1)
