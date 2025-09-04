#Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.

try:
    valor1 = int(input("Informe o primeiro número\n"))
    valor2 = int(input("Informe o segundo número\n"))

except: print("Por gentileza, informe números diferentes de zero e positivos")
else:
    print(f" {valor1} * {valor2} tem como resultado: {valor1*valor2}")