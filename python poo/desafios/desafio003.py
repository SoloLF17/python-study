from rich import print
from rich.panel import Panel

class Churrasco:

    def __init__(self, titulo="", quant =0):
        self.titulo = titulo
        self.quant = quant


    def analisar(self):
        preco = 82.40
        carne = self.quant * 0.4
        precot = carne * preco
        precop = precot / self.quant
        conteudo = (f"Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados [/]"
                f"\nCada participante comerá 0.4kg e cada Kg custa R${preco:.2f}"
                f"\nRecomendo [blue]comprar {carne:.3f}Kg[/] de carne"
                f"\nO custo total será de [green]R${precot:.2f}[/] de carne"
                f"\nCada pessoa pagará [yellow]R${precop:.2f}[/] para participar.")
        etiqueta = Panel(conteudo, title=self.titulo, width=60)
        print(etiqueta)


p = Churrasco("Churras dos Amigos", 15)
p.analisar()