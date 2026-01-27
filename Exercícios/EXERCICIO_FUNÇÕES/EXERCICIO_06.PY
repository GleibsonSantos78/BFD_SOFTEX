# Crie uma função chamada media que receba uma quantidade
# variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.


def media(*valor):

    return sum(valor) / len(valor)

print(f"Média de 3 valores:, {media(4, 8, 10)}")
print(f"Média de 5 valores:, {media(1, 2, 3, 4, 5)}") 
print(f"Média de 7 valores:, {media(10, 20, 30, 40, 50, 60, 70)}")
