# 1. Criando os jogadores (objetos independentes)
j1 = Jogador("Alisson", "Goleiro") # type: ignore
j2 = Jogador("Marquinhos", "Zagueiro") # type: ignore
j3 = Jogador("Vinícius Jr.", "Atacante") # type: ignore

# 2. Criando o time
meu_time = Time("Brasil FC")

# 3. Agregando os jogadores ao time
meu_time.contratar_jogador(j1)
meu_time.contratar_jogador(j2)
meu_time.contratar_jogador(j3)

# 4. Listando a equipe
meu_time.exibir_escalacao()