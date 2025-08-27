#contagem Crescente

# for x in range(1,11):
#           print(x)

#Tabuada

# tab = int(input("Digite um número de 1 a 10\n"))
# for x in range(1,11): 
#     y = tab * x
#     print(f"{tab} x {x} = {y}")

#Somatorio com While
# varsoma = 0
# while True:
#     num1 = float(input("Digite um número para somar (0 Para finalizar): "))
#     if num1 == 0:
#         break
#     varsoma += num1

# print("\nSomatória dos números digitados:", varsoma)

#Função de saudação
# nome = input("Digite seu nome aqui!")
# print(f"Olá,{nome}!")


# Define a função de saudação

# def saudar(nome):
#     print(f"Olá, {nome}!")

# x = input()

# saudar(x)

#Calculadora simples 

# Funções de operações
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    else:
       return a / b

# Menu de escolha
print("Calculadora Simples")
print("Escolha a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

# Entrada do usuário
opcao = input("Digite o número da operação desejada: ")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

# Executa a operação escolhida
if opcao == "1":
    resultado = somar(a, b)
elif opcao == "2":
    resultado = subtrair(a, b)
elif opcao == "3":
    resultado = multiplicar(a, b)
elif opcao == "4":
    resultado = dividir(a, b)
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print(f"\nResultado: {resultado}")