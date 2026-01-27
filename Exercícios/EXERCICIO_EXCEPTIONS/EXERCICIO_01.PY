# Escreva um programa que peça ao usuário para digitar um número.
# Trate o erro caso ele digite algo que não seja um número inteiro.


try:
    num = int(input("Digite um numero\n"))

except:
    print("Digite um numero, não um texto")
