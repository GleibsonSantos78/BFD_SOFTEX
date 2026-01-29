# 1. Criamos os funcionários de forma independente
f1 = Funcionario("Alice", "Desenvolvedora Senior")
f2 = Funcionario("Bruno", "Analista de Dados")
f3 = Funcionario("Carla", "Gerente de Projetos")

# 2. Criamos o Departamento
depto_ti = Departamento("Tecnologia da Informação")

# 3. Agregamos os funcionários já criados ao departamento
depto_ti.adicionar_funcionario(f1)
depto_ti.adicionar_funcionario(f2)
depto_ti.adicionar_funcionario(f3)

# 4. Exibimos a lista
depto_ti.listar_equipe()

# Demonstração de independência:
# Se deletarmos o objeto depto_ti, o objeto f1 continua existindo na memória.