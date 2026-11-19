from funcionarios import *

def main():
    f1 = FuncionarioHorista("Luiz", 8.5, 270)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = FuncionarioMensalista("Lucas", 9800)
    f2.calcular_salario()
    f2.analisar_salario()
if __name__ == "__main__":
    main()