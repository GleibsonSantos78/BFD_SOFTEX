# Mesclando dois dicionários

# Escreva uma função que recebe dois dicionários e retorna um novo
#  dicionário contendo todos os pares chave-valor. Se houver chaves
#  repetidas, o valor do segundo dicionário deve prevalecer.

def dicio_juntar(dic1,dic2):
    novo_dic = dic1.copy()
    novo_dic.update(dic2)
    return novo_dic


pessoa = {"nome": "Gleibson", "idade": 47,"CEP": 52280-180}
contato = {"nome": "Kevyn", "idade": 23, "email": "kevyn@dossantos.com"}

resultado = dicio_juntar(pessoa,contato)
print(resultado)