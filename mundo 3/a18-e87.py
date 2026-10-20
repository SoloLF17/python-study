matriz = [[0, 0, 0], [0, 0,0], [0, 0, 0]]
valorpar = tc = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l] [c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            valorpar += matriz[l] [c]
    print()
print('=' * 30)
print(f'A soma dos valores pares é {valorpar}.')
for l in range (0, 3):
    tc += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {tc}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda coluna é {maior}.')
