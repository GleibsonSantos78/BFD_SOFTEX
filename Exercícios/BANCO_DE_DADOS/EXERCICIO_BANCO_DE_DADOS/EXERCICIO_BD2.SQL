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


