# Interface em herança múltipla

# Crie uma interface Imprimivel com o método imprimir().
# Crie outra interface Exportavel com o método exportar(). 
# Implemente uma classe Relatorio que herde de ambas e implemente os métodos.


from abc import ABC, abstractmethod
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):...
class Exportavel(ABC):
    @abstractmethod
    def exportar(self):...

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        return print("Imprimindo relatório...")
    def exportar(self):
        return print("Exportando relatório...")
    
rel = Relatorio()
rel.imprimir()
rel.exportar()

