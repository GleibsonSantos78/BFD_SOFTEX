# Ordenando dicionário por valor

# Dado o dicionário:

# pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
# Imprima os itens do dicionário ordenados pela pontuação (valor),
#  do maior para o menor.


pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

ordenado = sorted(pontuacoes.items(),key=lambda item: item[1],reverse = True)

for nome, pontuacao in ordenado:
    print(f"{nome}: {pontuacao}")