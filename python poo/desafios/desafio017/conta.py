from hashlib import sha256
from rich import inspect, print


class ContaBancaria:
    """
    Cria uma conta Bancária e permite fazer saques e depósitos>
    """
    def __init__(self, id:int, nome:str = None, saldo:float = 0, chave:str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    def pede_senha(self):
        from pwinput import pwinput

        while True:
            senha = str(pwinput("Digite sua senha: ")).strip()
            if len(senha) >= 6:
                break
        return senha


    def validar_senha(self, chave):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False


    def __str__(self):
        return f'A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de saldo total.'


    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self._id}.")


    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"Depósito de R${valor:,.2f} na conta {self._id}.: SALDO INSUFICIENTE.")

            else:
                self.__saldo -= valor
                print(f"Saque de R${valor:,.2f} autorizado na conta {self._id}.")
        else:
            print("Senha incorreta. Saque não autorizado!")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome:str = None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novonome) >= 5:
                self._titular = novonome
        else:
            print("Senha invalida! Não podemos mudar o nome!")
