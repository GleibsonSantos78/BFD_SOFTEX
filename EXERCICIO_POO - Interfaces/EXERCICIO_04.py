# Forçando contrato

# Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id).
# Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos.
# O que acontece quando você tenta instanciá-la? Corrija o código


from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):...

    @abstractmethod
    def buscar(self, id):...

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        return print(f"Salvando {objeto} na memória.")
    def buscar(self, id):
        return print(f"Buscando objeto com id {id} na memória.")

repo = RepositorioMemoria()
repo.salvar("objeto1")
repo.buscar(1)

