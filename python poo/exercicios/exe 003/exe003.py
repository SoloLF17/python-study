from rich import inspect, print
class ContaBancaria:
    """
    Cria uma conta Bancária e permite fazer saques e depósitos>
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")
    def __str__(self):
        return f'A conta {self.id} de {self.nome} tem R${self.saldo:,.2f} de saldo total.'


    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}.")


    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Depósito de R${valor:,.2f} na conta {self.id}.: SALDO INSUFICIENTE.")

        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}.")

c1 = ContaBancaria(112, 'Luiz', 3000)
c1.depositar(500)
c1.sacar(1000)
print(c1)
inspect(c1)

