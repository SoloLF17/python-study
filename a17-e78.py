valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posicao {c}: ')))
    if c == 0:
        maior = menor = valores [0]
    else:
        if maior < valores [c]:
            maior = valores [c]
        if  menor > valores [c]:
            menor = valores [c]
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posicoes ', end= '')
for i,v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posicoes ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
