#def soma(a, b):
#    s = a + b
#   return s


#while True:
#    a = int(input('Digite um valor: '))
#    b = int(input('Digite outro valor: '))
#    res = soma(a, b)
#    print(f'A soma entre {a} e {b} é igual a {res}')
#    resp = str(input('Parar:[S/N] ')).strip().upper()[0]
#    if resp in 'Ss':
#      break

#def fatorial(num = 1):
#    f = 1
#    for c in range(num, 0,  -1):
#        f *= c
#    return f


#n = int(input('Digite um numero: '))
#print(f'O fatorial de {n} é igual a {fatorial(n)}')
#f1 = fatorial(5)
#f2 = fatorial (4)
#f3 = fatorial ()
#print(f'Os resultados são {f1}, {f2}, {f3}')


def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É par.')
else:
    print('É impar.')