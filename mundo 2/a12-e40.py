n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {} e {} sua media foi {:.1f}'.format(n1, n2, m))
if m < 5:
    print('REPROVADO')
elif m > 5 and m < 7:
    print('RECUPERACAO')
else:
    print('APROVADO')

