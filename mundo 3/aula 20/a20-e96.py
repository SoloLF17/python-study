def area(l, c):
    total = l * c
    print(f'A área de um terreno de {l} x {c} é de {total} m².')

def titulo(txt):
    print(txt)
    print('=' * 20)


titulo('CONTROLE DE TERRENO')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
