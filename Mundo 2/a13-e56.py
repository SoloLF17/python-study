soma = 0
media = 0
maioridh = 0
nomev = ''
totmulher = 0
for p in range (1,5):
    print('====== {} PESSOA ======'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridh = idade
        nomev = nome
    if sexo in 'Mm' and idade > maioridh:
        maioridh = idade
        nomev = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = soma / 4
print('A media de idade do grupo e de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridh, nomev))
print('Ao todo sao {} mulheres com menos de 20 anos.'.format(totmulher))
