a = int(input('Escolha o 1 n:'))
b = int(input('Escolha o 2 n:'))
c = int(input('Escolha o 3 n:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('o maior valor digitado foi {}.'.format(maior))
