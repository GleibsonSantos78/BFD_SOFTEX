# Peça ao usuário dois números e tente multiplicá-los.
# Se o usuário digitar algo inválido, exiba uma mensagem de erro.

try:
    num1 = float(input("Digite um numero\n"))
    num2 = float(input("Digite um numero\n"))
    valor = num1 * num2

    print(f"O resultado da multiplicação é: {valor}")
except ValueError:
    print("Digite um numero valido")
