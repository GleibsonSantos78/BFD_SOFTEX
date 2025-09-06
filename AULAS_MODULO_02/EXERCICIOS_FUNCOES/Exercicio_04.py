# Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:
# "Olá, [nome]!"
# Caso o nome não seja informado, mostre "Olá, visitante!".

def mensagem(nome="Visitante"):
    return print(f"olá, {nome}")

mensagem("josivaldo")
mensagem()