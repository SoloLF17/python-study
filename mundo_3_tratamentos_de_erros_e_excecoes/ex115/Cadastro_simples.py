from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # opção para cadastrar novas pessoas!
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3 :
        cabeçalho('Saindo do sistema... Até logo.')
        sleep(0.5)
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida!\033[m')
        sleep(2)
