from random import shuffle, choice

#Lê o nome dos jogadores e sorteia a sua ordem
jogadores = str(input('Digite o nome dos jogadores:')).split()
shuffle(jogadores)

quantidade = len(jogadores)
pessoas_grupo = quantidade / 2
grupos = 2

#Verificar se a quantidade de jogadores é par
if quantidade % 2 == 0:
    grupos_sorteados = [jogadores[i::grupos] for i in range(grupos)]
    print('GRUPO 1: {} \nGRUPO 2: {}'.format(grupos_sorteados [0], grupos_sorteados[1]) )

else:
    sobra = choice(jogadores)
    jogadores.remove(sobra)
    grupos_sorteados = [jogadores[i::grupos] for i in range(grupos)]
    print('GRUPO 1: {} \nGRUPO 2: {}'.format(grupos_sorteados[0], grupos_sorteados[1]))
    print('O jogador {} revezará a sua vez.'.format(sobra))