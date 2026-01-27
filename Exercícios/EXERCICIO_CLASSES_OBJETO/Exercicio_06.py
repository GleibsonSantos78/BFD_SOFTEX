# Modifique a classe ContaBancaria para que o método sacar
# True se a operação for bem-sucedida e False caso contrário.
# Teste o retorno e imprima mensagens adequadas.


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titula = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"\nOlá {self.titula}, Seu novo saldo é: {self.saldo}.")

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
        return True


operacao = ContaBancaria("João", 80)
valorsaque = 25

if operacao.sacar(valorsaque) == True:
    print(
        f"Saque de R$ {valorsaque} realizado com sucesso! saldo atual é de R$ {operacao.saldo} "
    )
else:
    print(
        f"Erro: saldo insuficiente para sacar R$ {valorsaque}, saldo atual é de R$ {operacao.saldo}."
    )
