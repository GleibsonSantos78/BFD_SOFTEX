lista = ["teste", "teste2"]
print(type(lista))

sala = lista
sala1 = lista[:]
sala2 = lista.copy

print(id(sala))
print(id(lista))
print(id(sala1))
print(id(sala2))

#inser adicionar item a lista
#append
#copy remove o ultimo item se não especificar o item
# clear apaga o conteudo da lista

lista.append("lima")
lista.insert(1,"limao")

print((lista))

#remover item
#del e remove

lista.remove("lima")
del lista[2]

print((lista))

#ordenar lista sort ordem

lista.sort()

#altera o nome do item da lista
lista[1] = "mangaba"