#Ordenação por comprimento da palavra (sorted + lambda)

#Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.

lista = ["uva", "banana", "maçã", "laranja"]

print(sorted(lista, key=lambda x: len(x)))

