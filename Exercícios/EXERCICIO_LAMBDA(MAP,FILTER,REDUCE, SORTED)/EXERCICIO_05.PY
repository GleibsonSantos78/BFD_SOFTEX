#Primeira letra maiúscula (map + lambda)

#Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].

lista = ["ana", "pedro", "maria"]
print(list(map(lambda nome: nome.capitalize(), lista)))

