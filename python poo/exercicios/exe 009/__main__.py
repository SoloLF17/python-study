from exe009 import Avaliacao
from rich import print, inspect


def main():
    av1 = Avaliacao("Pedro", "Matemática", 9.5)
    av1.set_nota(7.4)
    print(f"{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}")


if __name__ == '__main__':
    main()