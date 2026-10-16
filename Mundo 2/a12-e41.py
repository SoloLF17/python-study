from datetime import date
ano = int(input(' Ano do atleta: '))
anot = date.today().year
idade = anot - ano
print('Sua idade e {}'.format(idade))
if idade <= 9:
    print('Sua categoria e a MIRIM.')
elif idade <= 14:
    print('Sua categoria e a INFANTIL.')
elif idade <= 19:
    print('Sua categoria e a JUNIOR.')
elif idade <= 25:
    print('Sua categoria e a SENIOR.')
else:
    print('Sua categoria e a MASTER.')