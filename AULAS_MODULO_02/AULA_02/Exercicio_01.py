#01 - Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.

try:
    valor = int(input("Informe um número\n"))
except: print("POr gentileza, digite um número válido")
else:
    print(f"Agradecemos por você ter informado um número correto: {valor}")