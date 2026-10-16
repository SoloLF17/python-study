c1 = c2 = c3 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(' Sexo:[M/F] ')).strip().upper()[0]
    if idade >= 18:
        c1 += 1
    if sexo == 'M':
        c2 += 1
    if sexo == 'F' and idade < 20:
        c3 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {c1}
Ao todo temos {c2} homens cadastrados.
E temos {c3} mulheres com menos de 20 anos.''')
