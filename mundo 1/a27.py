n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome e {}'.format(nome[0]))
print('Seu ultimo nome e {}'.format(nome[len(nome)-1]))
