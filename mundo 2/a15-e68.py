from random import randint
soma = v = res = 0
print('-=' * 25)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 25)
while  True:
    n2 = randint(0,10)
    n1 = int(input('Diga um valor: '))
    soma = n1 + n2
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    if tipo == 'P':
        if soma % 2 == 0 :
            print('-' * 30)
            print(f'Voce jogou {n1} e o computador {n2}. O total de {soma} DEU PAR:')
            print('-' * 30)
            print('Voce ganhou')
            print('-' * 30)
            v += 1
        else:
            print('-' * 30)
            print(f'Voce jogou {n1} e o computador {n2}. O total de {soma} DEU IMPAR:')
            print('-' * 30)
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if soma % 2 == 0 :
            print('-' * 30)
            print(f'Voce jogou {n1} e o computador {n2}.O total de {soma} DEU PAR.')
            print('-' * 30)
            print('Voce perdeu.')
            break
        else:
            print('-' * 30)
            print(f'Voce jogou {n1} e o computador {n2}. O total de {soma} DEU IMPAR:')
            print('-' * 30)
            print('Voce ganhou.')
            print('-' * 30)
            v += 1
print('-=' * 30)
print(f'GAME OVER! Voce venceu {v} vezes.')






