# 10- Use input para receber 3 notas de dois alunos.
# As notas de cada aluno precisam ser armazenadas em uma lista separada que deve
# ser armazenada dentro de outra lista chamada notas, exemplo:
# notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

notas = []
João = []
Maria = []

print("João favor informar a 1ª Nota")
João.append(int(input()))
print("João favor informar a 2ª Nota")
João.append(int(input()))
print("João favor informar a 3ª Nota")
João.append(int(input()))

notas.append(João)

print("Maria favor informar a 1ª Nota")
Maria.append(int(input()))
print("Maria favor informar a 2ª Nota")
Maria.append(int(input()))
print("Maria favor informar a 3ª Nota")
Maria.append(int(input()))

notas.append(Maria)

MediaJoão = 0
MediaMaria = 0

for nota in notas:
    MediaJoão = sum(notas[0]) / len(notas[0])
    MediaMaria = sum(notas[1]) / len(notas[1])

print(f"A média de João é {MediaJoão} e de Maria é {MediaMaria} ")
