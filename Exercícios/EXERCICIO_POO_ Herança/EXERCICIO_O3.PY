# Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário".
# Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente".
# Mostre como funciona a chamada.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Email: {self.email}"
    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def saudacao(self):
        return "Olá, cliente"
    
cliente1 = Cliente("João", "joão@gmail.com")
    

print(cliente1.saudacao())