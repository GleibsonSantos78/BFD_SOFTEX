#Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

try:
    abrir_arquivo = open("Gleibson.txt, "r")
    ler_arquivo = abrir_arquivo.read()
except:
print("")
finally:
print(f"")
                         
