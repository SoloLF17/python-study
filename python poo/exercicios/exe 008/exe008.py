from rich import inspect, print
class ContaBancaria:
    """
    Cria uma conta Bancária e permite fazer saques e depósitos>
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")


    def __str__(self):
        return f'A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de saldo total.'


    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}.")


    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Depósito de R${valor:,.2f} na conta {self.id}.: SALDO INSUFICIENTE.")

        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}.")

