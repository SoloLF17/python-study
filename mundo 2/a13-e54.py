from datetime import date
m = 0
n = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {} nasceu: '.format(c)))
    idade = date.today().year - ano
    if idade > 18:
        m += 1
    else:
        n += 1
print('Das 7 pesoas {} sao maiores de idade e {} sao menores.'.format(m, n))
