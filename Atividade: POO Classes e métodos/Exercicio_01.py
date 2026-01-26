# Crie uma classe chamada Pessoa que tenha os atributos
# nome e idade. Em seguida, crie dois objetos dessa classe
# e imprima os valores de seus atributos.


class Pessoa:
    def __init__(self, nome="Josivaldo", idade=38):
        self.nome = nome
        self.idade = idade


atributos = Pessoa()

print(atributos.nome, atributos.idade)
