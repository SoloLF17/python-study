from exe010 import Avaliacao
from rich import print, inspect


def main():
    av1 = Avaliacao("Pedro", "Matemática")
    av1.nota = 5.5
    print(f"{av1.nome} tirou {av1.nota} em {av1.disciplina}")
    inspect(av1, private=True)

if __name__ == '__main__':
    main()