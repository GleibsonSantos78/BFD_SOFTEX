# Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro.
# Se o Carro deixar de existir, o Motor também deixa. Mostre isso criando e depois apagando o objeto.


class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print(f"Motor {self.tipo} está ligado!")


class Carro:
    def __init__(self, tipo_motor):
        # O Motor é criado dentro do Carro → COMPOSIÇÃO
        self.motor = Motor(tipo_motor)
        print(f"Carro criado com motor {self.motor.tipo}.")

    def dirigir(self):
        print(f"O carro com motor {self.motor.tipo} está em movimento.")
        self.motor.ligar()


# ===== Execução =====
carro1 = Carro("V8")
carro1.dirigir()

