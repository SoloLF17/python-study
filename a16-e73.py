times = ('corinthians', 'palmeiras','santos','gremio',
         'cruzeiro','flamengo', 'vasco', 'chapecoense',
         'atletico-mg', 'botafogo', 'atletico-pr', 'bahia',
         'sao paulo', 'fluminense','sport','vitoria',
         'coritiba', 'avai', 'ponte preta', 'atletico-go')
print('-=' * 20)
print(f'Lista de times: {times}')
print('-=' * 20)
print(f'Os 5 primeiros sao {times[0:5]}')
print('-=' * 20)
print(f'Os 4 ultimos sao {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 20)
print(f'O Chapecoense esta na {times.index("chapecoense") + 1} posicao')