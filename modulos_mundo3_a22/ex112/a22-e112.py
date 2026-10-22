from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

preço = dado.numero('Digite um preço:R$')
aumento = dado.numero('Quantos % de aumento: ')
desconto = dado.numero('Quantos % de desconto: ')
print(moeda.resumo(preço, 80, 40))