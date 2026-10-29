largura = 30
ceds = (200, 100, 50, 20, 10, 1)
print('=' * largura)
print(f'{"BANDO CEV":^{largura}}')
print('=' * largura)
valor = int(input('Qual valor deseja sacar:R$ '))
restante = valor
def quant (dados, ced):
    quantidade, restante = dados
    if quantidade > 0:
        print(f'{quantidade} cedulas de R${ced}')
    return None
[quant(divmod(restante, ced), ced) for ced in ceds ]
print('=' * largura)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

matriz = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]



# print('=' * 30)
# print('{:^30}'.format('BANCO CEV'))
# print('=' * 30)
# valor = int(input('Qual valor deseja sacar:R$'))
# total = valor
# ced = 50
# totced = 0
# while True:
#     if total >= ced:
#         total -= ced
#         totced += 1
#     else:
#         if totced > 0:
#             print(f'total de {totced} cedulas de R${ced}')
#         if ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1
#         totced = 0
#         if total == 0:
#             break
# print('=' * 30)
# print('Volte sempre ao BANCO CEV! Tenha um bom dia!')