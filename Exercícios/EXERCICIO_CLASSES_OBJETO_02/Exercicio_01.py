# Na classe, ContaBancaria, converta saldo para uma atributo privado.
# Crie um método setter e um getter para acessar e modificar essa atributo,
# seguindo uma regra lógica (Ex: saldo não pode ser negativo)


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

        # Getters

    def get_saldo(self):
        return self.__saldo

        # Setters

    def set_saldo(self, valor):
        if valor < 0:
            print("Saldo não pode ser negativo")
        else:
            self.__saldo = valor

    def depositar(self, valor):
        self.__saldo += valor
        print(f"\nOlá {self.titular}, Seu novo saldo é: {self.__saldo}.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print(
                f"\nOlá {self.titular}, seu saldo é insuficiente para saque!, saldo atual é: {self.__saldo}."
            )
        else:
            self.__saldo -= valor
        return print(f"\nOlá {self.titular}, seu saldo atual é: {self.__saldo}.")


operacao = ContaBancaria("João", 80)

print(operacao.get_saldo())

operacao.depositar(50)

operacao.sacar(20)
