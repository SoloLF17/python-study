from rich.panel import Panel
from rich import print

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favorito(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)


    def status(self):
        conteudo = f"Nome real: [green]{self.nome}[/]"
        conteudo += f"\nJogos Favoritos: "
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{game}[/]"
        painel = Panel(conteudo, title=f"[blue]Jogador {self.nick}[/]", width=50)
        print(painel)



j1 = Gamer("Luiz Felipe", "SoloLF17")
j1.add_favorito("Fifa 17")
j1.add_favorito("Cs2")
j1.add_favorito("COD: Warzone")
j1.add_favorito("Zelda")
j1.status()