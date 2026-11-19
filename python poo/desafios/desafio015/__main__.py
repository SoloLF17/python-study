from credencial import *

def main():
    c = Credencial()
    c.senha = str(input("Digite sua senha: "))

    c.validar("teste123")


if __name__ == '__main__':
    main()