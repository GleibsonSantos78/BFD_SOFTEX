# Crie uma classe, Pessoa, que tenha os atributos: nome,
# data de nascimento, cpf, identidade. Deixe os atributos
# Cpf e identidade como privado e monte os métodos setters e getters
# para acessar e editar os valores


class Pessoa:
    def __init__(self, nome, data_de_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_de_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    # getters
    def get_cpf(self):
        return self.__cpf

    def get_identidade(self):
        return self.__identidade

    # setters

    def set_cpf(self, valor):
        if len(str(valor)) == 11:
            self.__cpf = valor
        else:
            print("CPF deve ter 11 digitos")

    def set_identidade(self, valor2):
        if len(str(valor2)) == 6:
            self.__identidade = valor2
        else:
            print("Identidade deve ter 6 digitos")


pessoa1 = Pessoa("Josivaldo", "03/09/1987", 22222222222, 111111)

print(pessoa1.get_cpf())
print(pessoa1.get_identidade())

pessoa1.set_cpf(33333333333)
pessoa1.set_identidade(123456)

print(pessoa1.get_cpf())
print(pessoa1.get_identidade())
