from random import randint
from time import sleep
n2 = randint (0,5)
print('-=-'*20)
print('Irei pensar em um numero, tente advinhar!')
print('-=-'*20)
n1 = int(input('Em qual numero eu pensei: '))
print('PROCESSANDO...')
sleep(3)
if n1 == n2:
    print('parabens voce acertou e esse foi o numero sorteado {}.'.format(n2))
else:
    print('Ahh, que pena voce errou, eu pensei no {}'.format(n2))
