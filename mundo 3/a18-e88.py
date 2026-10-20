from time import sleep
from random import randint
lista = list()
jogos = list()
largura = '='*30
print(largura)
print('{:^30}'.format('JOGO NA MEGA SENA'))
print(largura)
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
sleep(0.4)
tot = 1
print('{:-^30}'.format(f'SORTEANDO {quant} jogos'))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    sleep(0.8)
    print(f'jogo {i + 1}: {l}')