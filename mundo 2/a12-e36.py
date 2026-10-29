v = float(input('valor da casa: R$'))
s = float(input('Salario do comprador: R$'))
a = int(input('Em quantos anos deseja financiar: '))
p = v / (a * 12)
n = s * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(v, a),end='')
print('a prestacao sera de R${:.2f}'.format(p))
if p <= n:
    print('EMPRESTIMO APROVADO!')
else:
    print('EMPRESTIMO NEGADO!')
