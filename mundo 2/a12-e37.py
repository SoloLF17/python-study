num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversao: 
[ 1 ] converter para BINARIO.
[ 2 ] converter para OCTAL.
[ 3 ] converter para HEXADECIMAL.''')
op = int(input('Sua opcao: '))
if op == 1:
    print('{} convertido para BINARIO e igual a {}.'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL e igual a {}.'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL e igual a {}.'.format(num, hex(num)[2:]))
else:
    print('OPCAO INVALIDA. TENTE NOVAMENTE')

