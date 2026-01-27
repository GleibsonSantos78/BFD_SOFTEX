# Crie uma classe Cachorro com um atributo de classe especie =
# "Canis familiaris" e atributos de instância nome e idade.
# Mostre a diferença entre acessar especie pelo objeto e pela classe.


class Cachorro:
    especie = "Canis familiaris"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


cao = Cachorro("Hulk", 3)


print(Cachorro.especie)

print(cao.especie)
