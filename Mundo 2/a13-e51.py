print('=' * 20)
print('10 TERMOS DE PA')
print('=' * 20)
termo = int(input('Qual o termo: '))
razao = int(input('Qual a razao: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Fim')
