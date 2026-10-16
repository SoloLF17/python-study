print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
c = 1
termo = primeiro
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    c += 1
print('FIM')
