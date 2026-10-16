frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))