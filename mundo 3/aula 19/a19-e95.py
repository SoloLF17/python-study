dados = dict()
partidas = list()
times = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {dados["nome"]} jogou: '))
    partidas.clear()
    for c in range(1, tot+1):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    times.append(dados.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! RESPONDA APENAS S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(times):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para finalizar) '))
    if busca == 999:
        break
    if busca >= len(times):
        print(f'ERRO! NÃO ECISTE JOGADOR COM CÓDIGO {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {times[busca]["nome"]}:')
        for i,g in enumerate(times[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-=' * 30)
print('<<< VOLTE SEMPRE >>>')