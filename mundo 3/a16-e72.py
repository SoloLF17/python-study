numero = ('zero', ' um', 'dois', ' tres', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezesseis', 'dezesete', 'dezoito',
          'dezenove', 'vinte')
while True:
    c = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= c <= 20:
        print(f'Voce digitou o numero {numero[c]}')
        res = str(input('Deseja continuar:[S/N] ')).strip().upper()[0]
        if res == 'N':
            break