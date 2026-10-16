print('-='*25)
print('Vamos saber quanto voce ira gastar na sua viagem.')
print('-='*25)
km = float(input('Qual a distancia em km da viagem? '))
if km <= 200:
    print('Voce ira gastar R${:.2f} nessa viagem de {}km' .format(km * 0.5, km))
else:
    print('Voce ira gastar R${:.2f} nessa viagem de {}km' .format(km * 0.45, km))
print('Aproveite bem a sua viagem!')
