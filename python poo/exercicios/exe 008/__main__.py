from exe008 import *

def main():
    c1 = ContaBancaria(112, 'Luiz', 5_000)
    c1.depositar(1_000)
    c1.sacar(100)
    print(c1)

if __name__ == '__main__':
    main()
