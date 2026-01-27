# Crie uma exceção personalizada chamada IdadeInvalidaError.
# Depois, crie uma função cadastrar_idade(idade) que lance essa exceção
# Caso a idade seja negativa.

class IdadeInvalidaError(Exception): ...

def cadastrar_idade():
    
    idade = int(input("Informe a sua Idade: "))
    if idade <= 0:
        raise IdadeInvalidaError("Idade não pode ser menor ou igual a zero")
    print(f"Idade {idade} cadastrada com sucesso!")

    return

cadastrar_idade()