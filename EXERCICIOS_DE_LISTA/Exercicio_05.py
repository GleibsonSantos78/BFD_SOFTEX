# 5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir,
# exiba a mensagem "Livro não encontrado".

livros = ["Odisseia","O Senhor dos Anéis","Harry Potter"]

if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
else:
    print("Livro não encontrado")