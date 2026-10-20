valor = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    opcao = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'voce digitou os valores {valor}')