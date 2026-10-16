nome = str(input('qual o seu nome:'))
if nome == 'luiz':
    print('Que nome bonito!')
elif nome == 'felipe' or nome == 'paulo' or nome == 'maria':
    print('Seu nome e bem popular.')
elif nome in 'ana claudia jessica juliana':
    print('belo nome feminino.')
else:
    print('seu nome e bem normal.')
print('tenha um bom dia, {}!'.format(nome))