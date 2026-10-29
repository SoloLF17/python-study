from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
print('''Suas opcoes
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Qual e a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador escolheu {}'.format(itens[maquina]))
print('Jogador escolheu {}'.format(itens[player]))
print('-=' * 11)
if maquina == 0: #pedra
    if player == 0:
        print('EMPATE')
    elif player ==1:
        print('JOGADOR VENCEU')
    elif player == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif maquina == 1: #papel
    if player == 0:
       print('COMPUTADOR VENCEU')
    elif player == 1:
        print('Empate')
    elif player == 2:
       print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif maquina == 2: #tesoura
    if player == 0:
        print('JOGADOR VENCEU')
    elif player == 1:
        print('COMPUTADOR VENCEU')
    elif player == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
