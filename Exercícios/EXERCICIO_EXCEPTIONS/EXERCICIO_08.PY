#Crie um programa que peça ao usuário um número inteiro e verifique se ele é par.
# Use:
# try para a conversão,
# else para verificar se é par ou ímpar,
# finally para exibir "Fim do programa".


try:
    num1 = int(input("Digite um número: "))

except ValueError:
    print("Erro: você deve digitar apenas números inteiros.")
else:
    if num1 % 2 == 0:
        print(f"O número digitado {num1} é par!")
    else:
        print(f"O número digitado {num1} é impar!")
finally:
    print("Fim do programa")