class Diario:

    def __init__(self, senhamestra = "Luiz"):
        self.__segredos = []
        self.__senha = senhamestra.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())


    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError("Senha incorreta")
        else:
            print(f"Diário Liberado!")
            for segredo in self.__segredos:
                print(f"- {segredo}")

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha!")

    @senha.setter
    def senha(self, novasenha):
        pass
