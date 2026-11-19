from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
class Funcionario(ABC):

    salario_minimo = 1_612
    desconto_inss = 7.5

    def __init__(self, nome = None,):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        base = self.salario / Funcionario.salario_minimo
        mensagem = f"O salário de [green]{self.nome}[/] ({self.__class__.__name__}) é de R${self.salario:.2f} e corresponde a [yellow]{base:.1f} salários minimos[/]"
        painel = Panel(mensagem, title="Análise de Salário", width=50)
        print(painel)

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, qtd_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtd_horas
        self.salario_bruto =self.valor_hora * self.horas_trabalhadas

    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.desconto_inss / 100)


class FuncionarioMensalista(Funcionario):
    def __init__(self,nome, salario_bruto = Funcionario.salario_minimo):
        super().__init__(nome)
        self.salario_bruto = salario_bruto



    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.desconto_inss / 100)

