#  Operadores Logicos NOT AND OR

# if True:
#     print("é o verdade esse bilhete")

# x = 6
# y = 5

# if x == y:
#      print("é verdade esse bilhete")

# elif x > y:
#     print("é maior")

# else:
#     print("é mentira")
#-----------------------------------------------------------------------
Idade = int(input("qual a sua idade: "))
carteira = input("Tem carteira de motorista? (SIM/não): ")
cachaca = input ("Ingeriu bebida alccolica? (SIM/não): ")

if Idade >= 18 and carteira == "sim" and cachaca == "não":
    print("vc pode dirigir")
else:
    print("vc não pode dirigir")