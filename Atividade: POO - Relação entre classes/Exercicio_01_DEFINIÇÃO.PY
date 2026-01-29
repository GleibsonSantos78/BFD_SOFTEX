class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livro_atual = None  # Aqui nasce a associação

    def ler_livro(self, livro):
        self.livro_atual = livro
        print(f"{self.nome} está lendo agora: {self.livro_atual}")