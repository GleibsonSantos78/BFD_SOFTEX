# Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:

#ValueError se o usuário digitar algo inválido

#ZeroDivisionError se tentar dividir por zero

try:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))
    soma = num1/num2
except ZeroDivisionError:
    print("O segundo valor precisa ser diferente de Zero")
except ValueError:
    print("Os valores precisam ser números")


