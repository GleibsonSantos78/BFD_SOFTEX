Criando uma interface

Crie uma interface chamada Pagamento com um método abstrato processar(valor). Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. Mostre como chamar processar() para cada uma.

Interface múltipla

Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). Crie uma classe Computador que implemente ambas. Mostre seu uso.

Interface em herança múltipla

Crie uma interface Imprimivel com o método imprimir(). Crie outra interface Exportavel com o método exportar(). Implemente uma classe Relatorio que herde de ambas e implemente os métodos.

Forçando contrato

Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. O que acontece quando você tenta instanciá-la? Corrija o código.