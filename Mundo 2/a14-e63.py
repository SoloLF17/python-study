print('=' * 25)
print('SEQUENCIA DE FIBONNACCI')
print('=' * 25)
n = int(input('Quanto termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' -> FIM', end='')