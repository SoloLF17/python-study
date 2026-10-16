from colorama import Fore, Back, Style, init
v = float(input('Qual a velocidade atual do carro? '))
if v > 80:
    a = (v - 80 ) * 7
    print(Fore.RED + '''MULTADO! Voce excedeu o limite permitido que e de 80km/h
    Voce deve pagar uma multa de R${:.2f}!'''.format (a))
print(Fore.GREEN + 'Tenha um bom dia! Continue dirijindo com seguranca!')


