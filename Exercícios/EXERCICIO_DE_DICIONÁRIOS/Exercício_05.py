# Verificando existência de uma chave

# Verifique se a chave "telefone" existe no dicionário:

contato = {"nome": "Ana", "email": "ana@email.com"}

if contato.get("telefone") == None:
    print("a chave: telefone não existe")
