from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import inspect
print("Ola,[red]Mundo[/]! :earth_americas:")
print("Ola, [bold blue on white] Pequeno Gafanhoto[/] :vulcan_salute:")
caixa = Panel("[white]Esse aqui é um painel de exemplo[/] :+1:", title="Exemplo", style="red", width=35)
print(caixa)

tabela = Table(title="Tabela de preços")

tabela.add_column("nome", justify="left", style="cyan")
tabela.add_column("preco", justify="center", style="green")
tabela.add_row("Lápis","R$1,50")
tabela.add_row("Borracha", "R$5,00")
print(tabela)
inspect(tabela)