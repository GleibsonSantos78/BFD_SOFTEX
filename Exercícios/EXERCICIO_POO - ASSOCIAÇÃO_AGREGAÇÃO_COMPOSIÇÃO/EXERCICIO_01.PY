# Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print(f"{self.nome} possui os seguintes livros:")
        for livro in self.livros:
            print(f" - {livro}")

livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Casmurro", "Machado de Assis")

pessoa1 = Pessoa("Ana")
pessoa1.adicionar_livro(livro1)
pessoa1.adicionar_livro(livro2)

pessoa1.listar_livros()

 
