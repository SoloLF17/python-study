from datetime import date
print('Deseja saber se um ano foi ou sera bissexto? Entao digite abaixo.')
ano = int(input('Ano? coloque 0 para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} e bissexto.'.format(ano))
else:
    print('O ano {} nao e bissexto.'.format(ano))