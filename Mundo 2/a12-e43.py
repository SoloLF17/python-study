print('-=' *  15)
print('IMC= Indice de massa coporal')
print('-=' * 15)
peso = float(input('Qual e o seu peso? (kG)'))
altura = float(input('Qual a sua altura? (M)'))
imc = peso / (altura ** 2)
print('O seu imc e {:.1f}'.format(imc))
if imc < 18.5:
    print('Cuidado voce esta abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('Parabens voce esta no peso ideal.')
elif 25 <= imc < 30:
    print('Cuidado voce esta com sobrepeso.')
elif 30 <= imc < 40:
    print('Atencao voce esta com obesidade.')
else:
    print('Atencao voce esta com obesidade morbida.')

