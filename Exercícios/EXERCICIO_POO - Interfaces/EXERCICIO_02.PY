# Interface múltipla

# Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()).
# Crie uma classe Computador que implemente ambas. Mostre seu uso.

from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):...
class Desligavel(ABC):
    @abstractmethod
    def desligar(self):...

class Computador(Ligavel, Desligavel):
    def ligar(self):
        return print("Computador ligado.")
    def desligar(self):
        return print("Computador desligado.")   
    

pc = Computador()
pc.ligar()
pc.desligar()
