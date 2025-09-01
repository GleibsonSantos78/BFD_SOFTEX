# Invertendo um dicionário

# Dado o dicionário:

# d = {"a": 1, "b": 2, "c": 3}
# Crie um novo dicionário invertendo
#  as chaves e os valores: {1: "a", 2: "b", 3: "c"}.

d = {"a": 1, "b": 2, "c": 3}
novo_d = {}

for chave, valor in d.items():
    novo_d[valor] = chave

print(novo_d)