# Dicionário com listas

# Crie um dicionário onde cada chave é o nome de um aluno
# e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.

alunos = {
    "Hillary": [8, 7, 9],
    "Emy": [6, 5, 7],
    "Kevyn": [9, 8, 10],
    "Gleibson": [4, 6, 5]
}

for aluno, nota in alunos.items():
    média = sum(nota) / len(nota)
    print(f" A nota de {aluno} é {média}")