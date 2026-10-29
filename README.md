<div align="center">

# Olá, eu sou o Luiz 👋

**Estudante de programação · Construindo minha base em Python**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Foco](https://img.shields.io/badge/Foco-Lógica_de_programação-FFD43B?style=for-the-badge&logoColor=black)
![Aprendizado](https://img.shields.io/badge/Aprendizado-Em_evolução-238636?style=for-the-badge)

Transformando curiosidade em código, um exercício de cada vez.

[Sobre mim](#sobre-mim) · [Conhecimentos](#conhecimentos-em-prática) · [Estudos](#meus-estudos) · [Próximos passos](#próximos-passos)

</div>

---

## Sobre mim

Sou o Luiz e estou desenvolvendo minha base em programação com Python. Estudo por meio de aulas, desafios e experimentos, colocando cada conceito em prática para entender como resolver problemas com código.

Meu foco atual é fortalecer o raciocínio lógico, explorar estruturas de dados e ganhar autonomia para construir minhas próprias soluções.

## Conhecimentos em prática

| Área | O que venho praticando |
| --- | --- |
| **Fundamentos de Python** | Variáveis, tipos de dados, entrada e saída, conversões e operadores |
| **Controle de fluxo** | Condições com `if`, `elif` e `else`; repetições com `for`, `while` e `break` |
| **Manipulação de textos** | Fatiamento, busca, separação de strings e formatação com f-strings |
| **Coleções** | Tuplas, listas e dicionários em exercícios de consulta, organização e manipulação de dados |
| **Funções** | Criação de funções, parâmetros, valores de retorno e reutilização de código |
| **Módulos e pacotes** | Organização de funções em módulos e importação de pacotes próprios |
| **Validação de dados** | Leitura e validação de valores digitados pelo usuário |
| **Tratamento de erros e exceções** | Uso de `try`, `except`, `else` e `finally` para lidar com entradas inválidas, divisão por zero e interrupções |
| **Arquivos** | Criação, leitura e gravação de cadastros em arquivos de texto |
| **Formatação de valores** | Cálculos de aumento, desconto e resumo de valores monetários |
| **Resolução de problemas** | Contadores, acumuladores, sequências numéricas e validação de entradas |
| **Biblioteca padrão** | Uso de `random`, `time` e `datetime` em exercícios |
| **Programação orientada a objetos** | Classes, objetos, atributos, métodos, construtores e representação de objetos com `__str__` |
| **Bibliotecas** | Apresentação de informações no terminal com a biblioteca `rich` |

## Meus estudos

### 🐍 Python · Curso em Vídeo

Registro minha evolução com exercícios organizados por etapas de aprendizado:

- **Mundo 1:** fundamentos, textos, cálculos e primeiras condições.
- **Mundo 2:** decisões, laços de repetição e desafios de lógica.
- **Mundo 3:** exercícios até o 106, com coleções, funções, módulos e pacotes.
- **Python POO:** primeiros exercícios e desafios com classes, objetos, atributos e métodos.

Entre os desafios que venho explorando estão jogos no terminal, verificadores de palíndromos, sequência de Fibonacci, simulação de caixa eletrônico e tabelas de preços. Também organizei utilidades para dados e moedas em módulos e pacotes próprios, pratiquei tratamento de exceções e arquivos e comecei a modelar situações do cotidiano com classes, como produtos, livros, contas bancárias e controles remotos.

### Organização do repositório

- [`mundo 1/`](mundo%201/) reúne os primeiros exercícios de Python.
- [`mundo 2/`](mundo%202/) concentra desafios de condições e estruturas de repetição.
- [`mundo 3/`](mundo%203/) reúne os exercícios do Mundo 3 até o 106, incluindo coleções e funções.
- [`modulos_mundo3_a22/`](modulos_mundo3_a22/) reúne exemplos de módulos, pacotes e utilidades reutilizáveis, incluindo os exercícios 107 a 112.
- [`mundo_3_tratamentos_de_erros_e_excecoes/`](mundo_3_tratamentos_de_erros_e_excecoes/) reúne os exercícios 113 a 115 sobre tratamento de exceções, validação de entradas, acesso a sites e cadastro persistido em arquivo.
- [`python poo/`](python%20poo/) contém exercícios e desafios introdutórios de programação orientada a objetos.

### Programação orientada a objetos

Na pasta [`python poo/`](python%20poo/) há exemplos de classes como `Gafanhoto`, `ContaBancaria`, `Produto`, `Livro`, `Caneta` e `ControleRemoto`. Os exercícios praticam criação de objetos, atributos de instância e de classe, métodos, construtores, representação textual e interação entre estado e comportamento. Alguns desafios usam `rich` para exibir painéis e informações coloridas no terminal.

Para executar um desafio de POO a partir da raiz do repositório:

```bash
python "python poo/desafios/desafio001.py"
```

### Tratamento de erros e exceções

Na pasta [`mundo_3_tratamentos_de_erros_e_excecoes/`](mundo_3_tratamentos_de_erros_e_excecoes/) estão os seguintes estudos:

- [`a23.py`](mundo_3_tratamentos_de_erros_e_excecoes/a23.py) demonstra o tratamento de erros ao ler números e realizar uma divisão, incluindo divisão por zero e interrupção pelo usuário.
- [`a23-e113.py`](mundo_3_tratamentos_de_erros_e_excecoes/a23-e113.py) cria as funções `leiaInt()` e `leiafloat()` para repetir a leitura até receber valores válidos.
- [`a23-e114.py`](mundo_3_tratamentos_de_erros_e_excecoes/a23-e114.py) verifica se um site está acessível usando `urllib`, tratando erros HTTP e de conexão.
- [`ex115/Cadastro_simples.py`](mundo_3_tratamentos_de_erros_e_excecoes/ex115/Cadastro_simples.py) implementa um menu para listar e cadastrar pessoas, com os dados armazenados em `ex115/cadastro.txt`.
- A pasta `ex115/lib/` separa as funções de interface e as operações com arquivos; `cadastro.txt` guarda os registros no formato `nome;idade`.
- [`teste.py`](mundo_3_tratamentos_de_erros_e_excecoes/teste.py) contém um pequeno teste com `range()`.

Para iniciar o cadastro do exercício 115 a partir da raiz do repositório:

```bash
python mundo_3_tratamentos_de_erros_e_excecoes/ex115/Cadastro_simples.py
```

O programa cria `cadastro.txt` caso não encontre o arquivo no diretório de execução.

Os arquivos são estudos independentes e podem ser executados individualmente com Python 3. Por exemplo:

```bash
python "mundo 3/a21-e106.py"
```

Alguns exercícios solicitam informações pelo terminal; basta seguir as instruções exibidas.

## Como estou aprendendo

```text
Estudar um conceito
       ↓
Resolver um desafio
       ↓
Executar e observar o resultado
       ↓
Revisar e continuar aprendendo
```

## Próximos passos

- [x] Praticar os fundamentos de Python.
- [x] Resolver exercícios com condições e repetições.
- [x] Explorar tuplas em desafios práticos.
- [x] Criar funções e organizar código em módulos e pacotes.
- [x] Iniciar os estudos de classes e objetos.
- [ ] Revisar exercícios anteriores com novos conhecimentos.
- [ ] Avançar nos conceitos de programação orientada a objetos e aplicar o que aprendi em projetos próprios.

---

<div align="center">

**Cada exercício é mais um passo na minha trajetória como programador.**

Luiz · Python · Aprendizado contínuo

</div>
