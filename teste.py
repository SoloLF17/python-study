lanche = ('hamburguer', 'pizza')
refri = ('coca-cola', 'fanta')
c = b = 0
bebida = comida = ' '
print('''MENU
[ 1 ] HAMBURGUER
[ 2 ] PIZZA''')
c = int(input('Selecione seu lanche: '))
if c == 1:
    comida = lanche[0]
else:
    comida = lanche[1]
print('''MENU
[ 1 ] COCA-COLA
[ 2 ] FANTA''')
b = int(input('Selecione sua bebida: '))
if b == 1:
    bebida = refri[0]
else:
    bebida = refri[1]
print(f'Ola! Voce escolheu {comida} e {bebida}.')
print('Um momento que iremos preparar o seu lanche.')


