aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}.')
if aluno['media'] >= 7:
    print(f'Parabéns {aluno["nome"]} você foi aprovado.')
elif 7 > aluno['media'] >= 5:
    print(f'{aluno["nome"]} infelizmente você está de recuperacao.')
else:
    print(f'{aluno["nome"]} você está reprovado')
