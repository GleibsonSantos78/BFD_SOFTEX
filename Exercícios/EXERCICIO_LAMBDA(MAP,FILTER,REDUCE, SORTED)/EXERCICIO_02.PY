#Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.
#Soma dos números (reduce + lambda)

lista = [10, 15, 20, 25, 30]
print(list(filter(lambda x: x % 2 == 0, lista)))
