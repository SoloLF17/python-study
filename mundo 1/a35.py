print('-=' * 20)
print('Analisador de Triangulos')
print('-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento:'))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima podem formar um triangulo.')
else:
    print('Os segmentos acima nao podem formar um triangulo.')