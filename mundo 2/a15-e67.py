while True:
    n = int(input('Escolha um numero para ver a tabuada: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('-' * 30)
print('Programa Tabuada encerado. Volte sempre!')
