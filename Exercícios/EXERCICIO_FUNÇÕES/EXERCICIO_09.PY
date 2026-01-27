# Crie uma função chamada aplicar_operacao que receba
# dois números e uma função como parâmetros. A função deve aplicar
#  a operação recebida (ex: soma, multiplicação). Exemplo:



def aplicar_operacao(a,b,operacao):
     return operacao(a, b)

def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print(aplicar_operacao(3, 4, soma))
print(aplicar_operacao(10, 5, subtracao))
print(aplicar_operacao(6, 7, multiplicacao))
print(aplicar_operacao(8, 2, divisao))



