from random import randint
n1 = randint(0, 10)
print('-=' * 20)
print('PENSEI EM UM NUMERO ENTRE 0 E 10 TENTE ADVINHAR: ')
print('-=' * 20)
n2 = int(input('Qual e o seu palpite: '))
c = 1
while n1 != n2:
    c += 1
    if n1 > n2:
        print('Mais...Tente outra vez')
    elif n1 < n2:
        print('Menos...Tente outraz vez')
    n2 = int(input('Qual e o seu palpite: '))
print('Voce levou {} tentativas para acertar meu numero escolhido que foi {}.'.format(c, n1))



