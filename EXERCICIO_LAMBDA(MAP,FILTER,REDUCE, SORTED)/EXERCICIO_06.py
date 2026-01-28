#Produto dos números (reduce + lambda)

#Usando reduce, calcule o produto (multiplicação) de todos os elementos da lista [2, 3, 4, 5].

from functools import reduce
lista = [2, 3, 4, 5]
print(reduce(lambda x, y: x * y, lista))
