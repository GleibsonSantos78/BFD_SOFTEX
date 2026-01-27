# 1 -  Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db

import sqlite3

conexao = sqlite3.connect("EXERCICIO_ATIVIDADE::_SQLite_NO_PYTHON/escola_v2.db")

# 2 - Faça a query para pegar toda a tabela alunos e imprima na tela.

cursor = conexao.cursor()
cursor.execute("SELECT * FROM aluno")

query_result = cursor.fetchall()
for linha in query_result:
    print(linha)


# 3 - Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas os 10 maiores notas.
# No fim imprima na tela a lista desses alunos e suas médias.

# cursor.execute("SELECT nome, (nota1 + nota2) / 2 AS media FROM aluno ORDER BY media DESC LIMIT 10")
query_result = cursor.fetchall()
for linha in query_result:
    print(linha)

# 4 - Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
cursor.execute("SELECT * FROM Aluno LEFT JOIN Turma ON Aluno.id_turma = Turma.id")
query_result = cursor.fetchall()
for linha in query_result:
    print(linha)

# 5 - Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.

cursor.execute(
    "SELECT * FROM Aluno LEFT JOIN Turma ON Aluno.id_turma = Turma.id WHERE Turma.id = 2"
)
query_result = cursor.fetchall()
for linha in query_result:
    print(linha)

conexao.close()
