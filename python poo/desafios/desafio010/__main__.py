from frete import *


def main():
    dist = 9

    entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}")

if __name__ == "__main__":
    main()