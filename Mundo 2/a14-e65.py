num = soma = cont = maior = menor = 0
res = 'S'
while res == 'S':
    num = int(input('Digite um valor:'))
    soma += num
    cont += 1
    if cont == 1:
       maior = menor = num
    else:
        if num > maior:
            meior = num
        if num < menor:
            menor = num
    res = str(input('Voce quer continuar?[S/N] ')).upper().strip()[0]
media = soma / cont
print('-=' * 30)
print('Voce digitou {} numeros e a media foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
print('FIM')
