from conta import *


def main():
    cc = ContaBancaria(111, "Luiz", 10000)
    print("Vou tentar sacar...")
    cc.sacar(500)

    print("Tentando mudar o nome...")
    cc.nome = "Felipe"
    print(cc)

if __name__ == "__main__":
    main()