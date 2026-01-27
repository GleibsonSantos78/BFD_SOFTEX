#Criando uma interface

# Crie uma interface chamada Pagamento com um método abstrato processar(valor).
#  Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface.
#  Mostre como chamar processar() para cada uma.

from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):...

class CartaoCredito(Pagamento):
    def processar(self, valor):
        return print(f"Processando pagamento de R${valor} no cartão de crédito.")

class Boleto(Pagamento):
    def processar(self, valor):
        return print(f"Gerando boleto para pagamento de R${valor}.")
cartao = CartaoCredito()
boleto = Boleto() 
cartao.processar(150.75)
boleto.processar(150.75)
