n1 = c = res = 0
while n1 != 999:
    n1 = int(input('Digite um numero [999 para parar]: '))
    if n1 != 999:
        res += n1
        n2 = res
        c += 1
    elif n1 == 999:
        print('Voce digitou {} numeros e a soma entre eles foi {}.'.format(c, res))
