class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"{self.nome} - {self.cargo}"

class Departamento:
    def __init__(self, nome_depto):
        self.nome_depto = nome_depto
        self.funcionarios = []  # Lista que guardará as referências dos objetos

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"Funcionário {funcionario.nome} alocado no departamento {self.nome_depto}.")

    def listar_equipe(self):
        print(f"\n--- Equipe do Departamento: {self.nome_depto} ---")
        for f in self.funcionarios:
            print(f)