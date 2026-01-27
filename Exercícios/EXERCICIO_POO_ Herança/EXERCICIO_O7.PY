# Usando o exemplo anterior, adicione um método status()
# em Autenticacao e também em Permissao. Se a classe Administrador
# herda das duas, qual versão de status() será chamada? Use Administrador.__mro__
# para mostrar a ordem.

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

    def status(self):
        print("Status de Autenticacao: Verificando credenciais.")

class Permissao:
    def verificar_permissao(self, usuario):
        if usuario == "admin":
            print("Permissão concedida.")
            return True
        else:
            print("Permissão negada.")
            return False

    def status(self):
        print("Status de Permissao: Verificando nível de acesso.")

class Administrador(Autenticacao, Permissao):
    def __init__(self, usuario, senha):
        super().__init__(usuario, senha)

    def acessar_sistema(self):
        if self.autenticar() and self.verificar_permissao(self.usuario):
            print("Acesso ao sistema permitido.")
        else:
            print("Acesso ao sistema negado.")

admin = Administrador("admin", "1234")
admin.status()
admin.acessar_sistema()

print("\nOrdem de resolução de métodos (MRO):")
for cls in Administrador.__mro__:
    print(cls)