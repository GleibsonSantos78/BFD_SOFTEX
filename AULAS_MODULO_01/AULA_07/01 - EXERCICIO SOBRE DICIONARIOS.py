#Crie um dicionário vazio chamado cadastro e adicione os seguintes pares chave-valor:
# "nome": "Lucas"
# "idade": 25
# "email": "lucas@email.com"

cadastro = {"nome": "Lucas","idade": 25,"email": "lucas@email.com"}

#Usando o dicionário abaixo, use o método .get() para obter o valor da chave "telefone",
#retornando "Não informado" se a chave não existir.

cliente = {"nome": "Amanda", "idade": 31}

if cliente.get("telefone") == None: print("Não informado")

#Utilize um laço for para imprimir todas as chaves do dicionário abaixo.

livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}

for livr in range(1): 
    chave = livro.keys() 
    print(chave)

#Adicione uma nova chave chamada "disponível" ao dicionário acima com o valor True.

livro["disponível"] = True

print(livro)

#Use o método .pop() para remover a chave "ano" do dicionário livro. Imprima o valor removido.

livro.pop("ano")

print(livro)

#Crie um dicionário compras com pelo menos 3 itens (nome do produto como chave e preço como valor).
#  Em seguida, use .values() para calcular o total da compra.

compras = {"Esponja":4.50, "Biscoito": 2.50, "Sabão": 8.30}

somacompras = sum(compras.values())

print(somacompras)

#Dado o dicionário: Imprima as frutas que têm mais de 2 unidades usando um laço for.

frutas = {"maçã": 3, "banana": 5, "laranja": 2}

for fruta, quantidad in frutas.items():
    if quantidad > 2:print(fruta)

#Verifique se a chave "senha" está presente no dicionário abaixo. Se não estiver,
# adicione-a com o valor "123456".

usuario = {"login": "joaosilva"}

if usuario.get("senha") == None: usuario["senha"] = 123456

print(usuario)

#Use o método .items() para iterar sobre o dicionário abaixo e imprima frases
#como "A capital de SP é São Paulo".

capitais = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}

for capital, capit in capitais.items():
        print(f"A capital de {capit} é {capit}")

#Dado o dicionário abaixo, atualize o valor da chave "estoque"
# somando 10 unidades ao valor atual.

produto = {"nome": "Teclado", "estoque": 15}

v = 10
for produto, somprod in produto.items():
     if somprod == "estoque": somprod
print(somprod + v)