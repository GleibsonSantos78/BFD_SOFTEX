# Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). 
# Use try e finally para garantir que uma mensagem de 
# "Encerrando programa" seja sempre exibida.

try:
    arquivo = open("dados.txt", "r")
    abrir = arquivo.read()
    print("Conteúdo do arquivo:")
    print(abrir)

except FileNotFoundError:
    print("O arquivo 'dados.txt' não encontrado.")

finally:
    print("Encerrando programa.")