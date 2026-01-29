# Criando os objetos (Instanciação)
from AULAS_MODULO_02.AULA_03.Exercicio_01 import Pessoa


escritor = Livro("O Alquimista", "Paulo Coelho") # type: ignore
leitor = Pessoa("Carlos")

# Demonstrando a associação: vinculamos o objeto 'escritor' ao atributo de 'leitor'
leitor.ler_livro(escritor)