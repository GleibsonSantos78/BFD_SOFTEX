#Crie uma função sacar(saldo, valor) que:

# Lance (raise) uma exceção personalizada 
# SaldoInsuficienteError se o valor for maior que o saldo.

# Caso contrário, retorne o novo saldo. 
# Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.


class SaldoInsuficienteError(Exception):...

def sacar(saldo, valor):

       if valor > saldo:

        raise SaldoInsuficienteError(print("Saldo insuficiente para realizar o saque."))
       
       return saldo - valor
        
try:
    num1 = int(input("Digite o valor de Saque\n"))
    novo_saldo = sacar(50,num1)
    print(f"\nSaque realizado com sucesso! Novo saldo: R$ {novo_saldo}\n")

except (NameError, ValueError):
    print(f"\nErro: favor digite um numero inteiro")