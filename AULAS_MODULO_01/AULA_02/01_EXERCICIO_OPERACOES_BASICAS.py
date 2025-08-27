# Programa de Operações Basicas

#Dados

Entrada1 = float(input("Digite um numero: "))
Entrada2 = float(input("Digite um numero: "))

#Calculo
Soma = Entrada1 + Entrada2
Subtracao = Entrada1 - Entrada2
Multiplicacao = Entrada1 * Entrada2

if Entrada2 != 0:
    Divisao = Entrada1 / Entrada2
else:
    Divisao = "Erro: divisão por zero"

# Saída dos resultados

print("\nResultados das operações:")
print(f"Adição: {Soma}")
print(f"Subtração: {Subtracao}")
print(f"Multiplicação: {Multiplicacao}")
print(f"Divisão: {Divisao}")