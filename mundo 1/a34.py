s = float(input('Qual e o salario do funcionario? R$'))
if s > 1250:
    print('O seu salario aumentou de R${:.2f} para R${:.2f}.'.format(s, (s / 100 *10) + s))
else:
    print('O seu salario aumentou de R${:.2f} para R${:.2f}.'.format(s, (s / 100 * 15) + s))
