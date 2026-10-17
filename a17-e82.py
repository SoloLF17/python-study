lista = list()
pares = list()
impar = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if r == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impar}')