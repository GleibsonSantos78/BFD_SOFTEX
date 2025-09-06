# Crie uma função chamada calculadora que tenha dentro dela outras funções
# somar, subtrair, multiplicar, dividir). A função principal deve permitir
# escolher a operação e retornar o resultado.


def calculadora():
    def somar(x, y):
        return x + y

    def subtrair(x, y):
        return x - y

    def multiplicar(x, y):
        return x * y

    def dividir(x, y):
        if y == 0:
            return "Erro: divisão por zero"
        return x / y

    while True:
        print("\nOperações disponíveis: soma | subtracao | multiplicacao | divisao | sair")
        operacao = input("Escolha a operação: ").lower()

        if operacao == "sair":
            print("Encerrando a calculadora. Até mais!")
            break
        if operacao not in ["soma", "subtracao", "multiplicacao", "divisao"]:
            print("Por favor, escolha uma operação válida.")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        match operacao:
            case "soma":
                resultado = somar(a, b)
            case "subtracao":
                resultado = subtrair(a, b)
            case "multiplicacao":
                resultado = multiplicar(a, b)
            case "divisao":
                resultado = dividir(a, b)
            case _:
                print("Operação inválida. Tente novamente.")
                continue

        print(f"Resultado: {resultado}")


calculadora()