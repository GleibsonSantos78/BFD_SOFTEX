# Crie uma classe Funcionario que herda de Usuario e, em seguida,
# crie uma classe Gerente que herda de Funcionario. Mostre como
# instanciar um gerente e acessar seus atributos.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Funcionario(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

class Gerente(Funcionario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

gerente = Gerente("Ana Silva", "as@gmail.com")

print(gerente.nome)
print(gerente.email)