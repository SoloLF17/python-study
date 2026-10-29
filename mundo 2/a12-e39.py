from datetime import date
ano = int(input('Ano de nascimento: '))
at = date.today().year
idade = at - ano
if idade < 18:
    i = 18 - idade
    al = at + i
    print('''Quem nasceu em {} tem {} em {}.
    Ainda faltam {} para o alistamento.
    Seu alistamento sera em {}.'''.format(ano, idade, at, i, al))
elif idade > 18:
    i = idade - 18
    al = at - i
    print('''Quem nasceu em {} tem {} em {}.
    Voce ja deveria ter se alistado ha {} anos.
    Seu alistamento foi em {}.'''.format(ano, idade, at, i, al))
else:
    print('''Quem nascem em {} tem {} em {}.
    voce tem que se alistar IMEDIATAMENTE.'''.format(ano, idade, at))

