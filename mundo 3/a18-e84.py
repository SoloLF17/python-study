dados = list()
np = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append((float(input('Peso: '))))
    if len(np) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    np.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Ao todo, voce cadastrou {len(np)} pessoas.')
print(f'O maior peso foi de {maior:.2f}Kg. Peso de ', end='')
for p in np:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {menor:.2f}Kg. Peso de ', end='')
for p in np:
    if p[1] == menor:
        print(f'[{p[0]}]')

