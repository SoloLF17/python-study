from retangulo import *

def main():
    r = Retangulo()
    try:
        r.altura = 12
        r.base = 7
        r.medidas(8,12)
    except Exception as e:
        print(f" Ocorreu um erro: {e}")

    print(r.medidas)


if __name__ == "__main__":
    main()