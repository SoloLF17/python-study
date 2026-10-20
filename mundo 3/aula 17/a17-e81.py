lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('=' * 20)
print(f'Foram digitados {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {lista}')
if 5 in lista:
    print('O valor 5 faz parte lista.')
else:
    print('O valor 5 nao faz parte da lista.')

