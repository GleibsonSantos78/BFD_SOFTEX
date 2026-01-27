-- Revisão aula 01 de Banco de dados


-- comando para listar tabela
.tables

.schema Aluno
.schema Curso
.schema Turma

Select * from aluno;


Select count(*) from aluno;
Select Max(nota1) from aluno;
Select Min(nota1) from aluno;
Select Sum(nota2) from aluno;
Select Avg(nota1) from aluno;


SELECT nome FROM Aluno WHERE nome LIKE '%Feli%';


