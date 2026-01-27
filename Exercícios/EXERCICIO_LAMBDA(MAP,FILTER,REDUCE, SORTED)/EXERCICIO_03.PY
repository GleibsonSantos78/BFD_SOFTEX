#Soma dos números (reduce + lambda)

#Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].

from functools import reduce

lista = [1,2,3,4,5]
print((reduce(lambda x, y : x + y, lista)))