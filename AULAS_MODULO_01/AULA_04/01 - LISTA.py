# #teste Lista


# #frutas = ["banana", "manga", "maça","jaca"]
# # frutas.insert(6,"laranja")
# tempero = ["sal","pimenta"]
# # tempero += frutas

# #print((frutas))
# # remover itens da lista

# #frutas.remove("jaca")
# #del frutas[1]


# #print((frutas))
# #print(frutas[0:3])
# #print((tempero))
# #ordenar listar

# frutas = ["banana", "manga", "maça","jaca"]
# #print(sorted(frutas))
# frutas.sort
# print(frutas)


# salada_de_frutas = frutas

# print(id(salada_de_frutas))


#copiar

frutas = ["banana", "manga", "maça","jaca","jaca","jaca"]
salada = ["morango","uva"]

#salada = frutas[:]

# print(id(salada))
# print(id(frutas))

# for fruta in frutas:
#     salada.append(fruta)

# print(salada)
# print(frutas)

# print(id(salada))
# print(id(frutas))


#salada = frutas.copy

#print(frutas.count("maça"))

#print(id(salada))
#print(id(frutas))

#juntar a lista
salada.extend(frutas)

print(frutas)
print(frutas.index("jaca"))

idx_jaca = frutas.index("jaca")

del frutas[idx_jaca]

print(frutas)