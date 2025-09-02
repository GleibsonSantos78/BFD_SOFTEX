"""11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial.
Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:

[ ] - para posições vazias
tor - para a torre
cav - para o cavalo
bis - para o bispo
rai - para a rainha
rei - para o rei
pea - para o peão
Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra.
Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)"""

import numpy as np

tabuleiro = [["[ ]" for linha in range(8)] for coluna in range(8)]

pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]

tabuleiro[0] = [p for p in pecas]
tabuleiro[1] = [ "pea" for linha in range(8)]


tabuleiro[7] = [p for p in pecas]
tabuleiro[6] = ["pea" for linha in range(8)] 


print(np.array(tabuleiro))