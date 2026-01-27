-- Mostre todos os registros da tabela Aluno. (Use SELECT e FROM)
Select * from Aluno;

-- Exiba apenas o nome e a nota1 de todos os alunos. (Use SELECT com colunas específicas)
Select nome, nota1 from Aluno;

-- Liste todos os alunos cuja nota2 seja maior que 8. (Use WHERE)
Select nome, nota2 from Aluno WHERE nota2 > 8;

-- Mostre os alunos que nasceram após o ano de 2000. (Use WHERE com data)
Select nome, data_nascimento from Aluno WHERE SUBSTR(data_nascimento,1,4) >= '2000';

-- Exiba o nome e a mensalidade de todos os cursos que custam mais de 600 reais. (Use WHERE com condição numérica)
Select nome, mensalidade from Curso WHERE mensalidade > 600;

-- Mostre o nome das turmas e o ano correspondente, ordenados pelo ano em ordem crescente. (Use ORDER BY)
Select nome, ano from Turma ORDER BY ano ASC;

-- Liste o ano das turmas e a quantidade de turmas por ano. (Use GROUP BY)
Select ano, count(*) as quantidade_turmas from Turma GROUP BY ano;

-- Calcule a média da nota1 dos alunos por turma_id. (Use GROUP BY com função de agregação)
Select id_turma, Avg(nota1) as media_nota1 from Aluno GROUP BY id_turma;

-- Mostre o ano e a quantidade de turmas apenas para os anos que têm mais de 2 turmas. (Use GROUP BY e HAVING)
Select ano, count(*) as quantidade_turmas from Turma GROUP BY ano HAVING quantidade_turmas > 2;

-- Exiba o nome dos cursos e suas mensalidades, ordenando primeiro pela mensalidade (decrescente). (Use ORDER BY)
Select nome, mensalidade from Curso ORDER BY mensalidade DESC;

-- COUNT Mostre quantos alunos estão cadastrados na tabela Aluno. (Use a função COUNT)
SELECT count(*) from Aluno;

-- MIN Mostre a menor mensalidade entre todos os cursos cadastrados. (Use a função MIN)
Select MIN(mensalidade) from Curso;

-- MAX Mostre a maior nota1 registrada entre todos os alunos. (Use a função MAX)
Select MAX(nota1) from Aluno;

-- SUM Calcule o valor total das mensalidades de todos os cursos. (Use a função SUM)
Select SUM(mensalidade) from Curso;

-- AVG Mostre a média geral da nota2 dos alunos. (Use a função AVG)
Select AVG(nota2) from Aluno;


