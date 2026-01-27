# Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.Departamento deve agregar funcionários já criados.


class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"{self.nome} - {self.cargo}"


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        
    def listar_funcionarios(self):
        print(f"Departamento: {self.nome}")
        for funcionario in self.funcionarios:
            print(f" - {funcionario}")


func1 = Funcionario("Maria", "Analista")
func2 = Funcionario("João", "Desenvolvedor")
func3 = Funcionario("Ana", "Gerente")
dept = Departamento("TI")
dept.adicionar_funcionario(func1)
dept.adicionar_funcionario(func2)
dept.adicionar_funcionario(func3)
dept.listar_funcionarios()

 
