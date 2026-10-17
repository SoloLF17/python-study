import os
import time

matriz = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]

linhas = 3
colunas = 4
intervalo = 0.4
def limpar_tela():
    os.system ("cls")

def mostrar_matriz(matriz):
    for linha in matriz:
        print(' | '.join(f'{nome:^8}' for nome in linha))
        print('=' * 30)
def animar():
    coluna_atual = 0

    try:
        while True:
            matriz = [
                [''] * colunas
                for _ in range(linhas)
            ]
            for linha in range(linhas):
                matriz[linha][coluna_atual] = "luiz"
            limpar_tela()
            print('Animacao')
            mostrar_matriz(matriz)
            time.sleep(intervalo)
            coluna_atual = (coluna_atual + 1) % colunas
    except KeyboardInterrupt:
        print('Acabou')
if __name__ == '__main__':
    animar()






