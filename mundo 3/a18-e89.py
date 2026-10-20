ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2= float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}.')