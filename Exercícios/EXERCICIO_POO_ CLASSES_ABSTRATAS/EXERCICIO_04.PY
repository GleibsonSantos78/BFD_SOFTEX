#Herança parcial

# Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar().
# Depois, crie uma subclasse Carro que implemente apenas o método mover().
#  O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.


from abc import ABC, abstractmethod
class Transporte(ABC):
    @abstractmethod
    def mover(self):...

    @abstractmethod
    def parar(self):...

class Carro(Transporte):
    def mover(self):
        return print("O carro está se movendo.")
    def parar(self):
        return print("O carro parou.")
    
carro = Carro()
carro.mover()
carro.parar()

