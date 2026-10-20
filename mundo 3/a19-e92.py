from datetime import date
n = 0
cad = dict()
cad['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cad['idade'] = date.today().year - nasc
cad['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cad['ctps'] != 0:
    cad['contratação'] = int(input('Ano de contratação: '))
    cad['salario'] = float(input('Salario:R$'))
    cad['aposentadoria'] = cad['idade'] + (cad['contratação'] + 35) - date.today().year
    print('=' * 50)
    for k, v in cad.items():
        print(f'  - {k} tem o valor {v}')

