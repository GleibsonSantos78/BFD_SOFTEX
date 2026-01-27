# Na classe Cliente, adicione o atributo saldo.
# Adicione um método construtor em Cliente que inicialize
# também os atributos de Usuario usando super().

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Cliente(Usuario):
    def __init__(self, nome, email, saldo=33):
        super().__init__(nome, email)
        self.saldo = saldo

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Email: {self.email}, saldo: {self.saldo}"

    
cliente1 = Cliente("João", "joão@gmail.com")

print(cliente1.exibir_informacoes())
