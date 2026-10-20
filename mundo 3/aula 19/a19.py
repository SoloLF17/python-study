#pessoas = {'nome':'Luiz', 'sexo':'M', 'idade': 26}
#pessoas['Peso'] = 74
#for k in pessoas.keys():
    #print(k)
#for v in pessoas.values():
    #print(v)
#for k, v in pessoas.items():
    #print(f'{k} = {v}')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
