from time import sleep
n = int(input('Digite um numero para calcular seu fatorial:'))
c = n
f = 1
print('Calculando {}!.'.format(n))
sleep(1)
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))