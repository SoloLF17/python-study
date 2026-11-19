from rich import print,inspect
from classex005 import Aluno, Professor, Funcionario


def main():
    a1 = Aluno("Josue", 21, "administração", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()


    p1 = Professor ("samuel", 28, "Biologia", "Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()


    f1 = Funcionario("Luiz", 27, "programador","TI")
    f1.fazer_aniversario()
    f1.bater_ponto()

if __name__ == "__main__":
    main()