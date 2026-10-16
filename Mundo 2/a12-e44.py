print('========LOJAS GUANABARA=========')
valor = float(input('Qual o valor da compra: R$'))
print('''   FORMA DE PAGAMENTO 
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA CARTAO
[ 3 ] 2x NO CARTAO
[ 4 ] 3x OU MAIS NO CARTAO''')
opcao = int(input('Qual e a opcao?'))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    res = total / 2
    print('Sua compra sera parcela em 2x de R${:.2f} sem juros.'.format(res))
elif opcao == 4:
    pa = int(input('Quantas parcelas? '))
    total = valor + (valor * 20 /100)
    par = total / pa
    print('A sua compra sera parcelada em {}x de R${:.2f} COM JUROS.'.format(pa, par))
else:
    total= valor
    print('OPCAO INVALIDA de pagamento. Tente Novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))

