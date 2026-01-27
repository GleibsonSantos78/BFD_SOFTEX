# Dicionário com listas

# Crie um dicionário onde cada chave é o nome de um aluno
# e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.

alunos = {
    "Ana": [8, 7, 9],
    "Bruno": [6, 5, 7],
    "Carla": [9, 8, 10],
    "Daniel": [4, 6, 5],
}

for aluno, nota in alunos.items():
    média = sum(nota) / len(nota)
    print(f" A nota de {aluno} é {média}")
