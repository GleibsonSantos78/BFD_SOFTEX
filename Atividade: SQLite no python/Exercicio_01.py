import sqlite3

# 1. Conexão com o banco de dados escola_v2.db
conexao = sqlite3.connect('escola_v2.db')
cursor = conexao.cursor()

print("--- QUESTÃO 2: Toda a tabela Alunos ---")
# 2. Query para pegar toda a tabela alunos
cursor.execute("SELECT * FROM Aluno")
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)

print("\n--- QUESTÃO 3: Top 10 Médias (Decrescente) ---")
# 3. Média entre nota1 e nota2, ordenado, limite 10
# Nota: (nota1 + nota2) / 2.0 garante que o cálculo use ponto flutuante
query_media = """
SELECT nome, (nota1 + nota2) / 2.0 AS media 
FROM Aluno 
ORDER BY media DESC 
LIMIT 10
"""
cursor.execute(query_media)
top_10 = cursor.fetchall()
for registro in top_10:
    print(f"Aluno: {registro[0]} | Média: {registro[1]:.2f}")

print("\n--- QUESTÃO 4: Left Join Aluno e Turma ---")
# 4. Left Join para trazer todos os dados (mesmo alunos sem turma ou turmas vazias)
query_join = """
SELECT * FROM Aluno 
LEFT JOIN Turma ON Aluno.turma_id = Turma.id
"""
cursor.execute(query_join)
dados_completos = cursor.fetchall()
for linha in dados_completos:
    print(linha)

print("\n--- QUESTÃO 5: Filtro Turma 2 ---")
# 5. Mesma query anterior com filtro WHERE
query_filtro = """
SELECT * FROM Aluno 
LEFT JOIN Turma ON Aluno.turma_id = Turma.id 
WHERE Aluno.turma_id = 2
"""
cursor.execute(query_filtro)
turma_2 = cursor.fetchall()
for aluno_t2 in turma_2:
    print(aluno_t2)

# Fechando a conexão
conexao.close()