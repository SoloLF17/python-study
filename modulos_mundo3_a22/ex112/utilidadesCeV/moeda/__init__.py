def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)

def aumentar(preço=0, taxa=0, formato=False):
    res = 0
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = 0
    res = preço - (preço * taxa / 100 )
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


def resumo(preço=0, taxaA=0, taxaD=0):
    titulo('  RESUMO DO VALOR')
    a = preço
    return (f'Preço analisado: {moeda(a)}'
            f'\nDobro do preço:  {dobro(a, formato=True)}'
            f'\nMetade do valor: {metade(a, formato=True)}'
            f'\n{taxaA}% de aumento:  {aumentar(a, taxaA, formato=True)}'
            f'\n{taxaD}% de redução:  {diminuir(a, taxaD, formato=True)}')
