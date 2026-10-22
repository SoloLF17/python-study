from ex110 import moeda

preço = int(input('Digite um preço:R$'))
aumento = int(input('Quantos % de aumento: '))
desconto = int(input('Quantos % de desconto: '))
print(moeda.resumo(preço, aumento, desconto))