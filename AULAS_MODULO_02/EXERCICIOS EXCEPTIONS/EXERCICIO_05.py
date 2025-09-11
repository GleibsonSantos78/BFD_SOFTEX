# Crie uma função dividir(a, b) que lance (raise) 
# uma exceção ZeroDivisionError se b for igual a zero. 
# Caso contrário, retorne o resultado da divisão.

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("O segundo valor precisa ser diferente de Zero")
    return a / b