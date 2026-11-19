from personagem_rpg import *

def main():
    p1 = Guerreiro("Solo", 150)
    p2 = Mago("Han", 150)
    p1.atacar(p2,100)
    p2.atacar(p1,100)
    p1.curar()
    p2.curar()


if __name__ == "__main__":
    main()
