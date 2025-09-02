#Acessando valores
#Dado o dicionário:
#produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
#Imprima o nome do produto e a quantidade em estoque.

produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}

for chave, valor in produto.items():
    print(f"{chave}: {valor}")