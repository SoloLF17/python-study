from time import sleep
def maior(* num):
    cont = m = 0
    print('=' * 20)
    print('ANALISANDO OS VALORES:')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            m = valor
        else:
            if valor > m:
                m= valor
        cont += 1
    print(f'Foram informados. E {cont} valores ao todo.')
    print(f'O maior valor foi {m}')


maior(2, 9, 4, 5, 7 , 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
