# my solution

import random
import sys

def dealer(player, n):
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(0, n):
        player.append(random.choice(cartas))

jogador = []
mesa = []

# 1 rodada
dealer(mesa, 2)
print(f'as cartas da mesa são [{mesa[0]},X]')
dealer(jogador, 2)
print(f'Suas cartas são {jogador}\n')

blackjack = ''

if 11 in jogador and 10 in jogador:
    print('Você tem Blackjack!\nVocê ganhou!')
    sys.exit(0)
elif 11 in mesa and 10 in mesa:
    blackjack = 'table'

# jogadas do jogador
jpontos = sum(jogador)
jogadas = True
while jogadas:
    if 11 in jogador and jpontos > 21:
        jogador.remove(11)
        jogador.append(1)
    a = input('Deseja outra carta? (s/n) ')
    if a == 's' or a == 'S':
        dealer(jogador, 1)
        jpontos = sum(jogador)
        print(f'Sua mão é {jogador}')
    else:
        jpontos = sum(jogador)
        print(f'Sua soma é {jpontos}')
        jogadas = False
    if jpontos > 21:
        print('Você estourou!')
        sys.exit(0)

print(f'As cartas da mesa são {mesa}')

if blackjack == 'table':
    print('A mesa tem Blackjack!\nVocê perdeu!')
    sys.exit(0)


# jogadas da mesa
mpontos = 0
while mpontos < 17:
    dealer(mesa, 1)
    mpontos = sum(mesa)
    print(f'As cartas da mesa são {mesa}')
    if mpontos > 21:
        print('A mesa estourou.')
        jogadas = False
        sys.exit(0)

if jpontos > mpontos:
    print('Você Ganhou!')
elif mpontos > jpontos:
    print('A Mesa Ganhou!')
else:
    print('Empate')
