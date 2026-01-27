#Proibição de instanciamento

# Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):...


animal = Animal()

# Quando uma classe é abstrata em Python, ela não pode ser instanciada diretamente.
# Isso serve para garantir que apenas classes filhas que implementem completamente os métodos abstratos possam ser usadas para criar objetos.

