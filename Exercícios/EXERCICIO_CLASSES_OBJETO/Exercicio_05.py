# Crie uma classe ContaBancaria com os atributos titular e saldo.
# Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor)
# Que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titula = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"\nOlá {self.titula}, Seu novo saldo é: {self.saldo}.")

    def sacar(self, valor):
        if valor > self.saldo:
            print(
                f"\nOlá {self.titula}, seu saldo é insuficiente para saque!, saldo atual é: {self.saldo}."
            )
        else:
            self.saldo -= valor
        return print(f"\nOlá {self.titula}, seu saldo atual é: {self.saldo}.")


operacao = ContaBancaria("João", 80)

operacao.depositar(50)

operacao.sacar(20)
