from rich import inspect
from diario import *

def main():
    d = Diario()
    d.escrever("Esse é a primera mensagem")
    d.escrever("Estou aprendendo Python")

    try:
        d.ler("Luiz")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == '__main__':
    main()