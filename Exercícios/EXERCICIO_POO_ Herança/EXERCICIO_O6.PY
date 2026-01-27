# Crie uma classe Autenticacao com um método login().
# Crie outra classe Permissao com um método verificar_permissao().
# Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?.

class Autenticacao:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def autenticar(self):
        if self.usuario == "admin" and self.senha == "1234":
            print("Login bem-sucedido!")
            return True
        else:
            print("Login falhou.")
            return False

class Permissao:
    def verificar_permissao(self, usuario):
        if usuario == "admin":
            print("Permissão concedida.")
            return True
        else:
            print("Permissão negada.")
            return False

class Administrador(Autenticacao, Permissao):
    def __init__(self, usuario, senha):
        super().__init__(usuario, senha)

    def acessar_sistema(self):
        if self.autenticar() and self.verificar_permissao(self.usuario):
            print("Acesso ao sistema permitido.")
        else:
            print("Acesso ao sistema negado.")

admin = Administrador("admin", "1234")
admin.acessar_sistema()



