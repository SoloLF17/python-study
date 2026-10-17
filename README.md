<div align="center">

# Python · Jornada de aprendizado

**Lógica, prática e evolução — um exercício de cada vez.**

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Foco](https://img.shields.io/badge/Foco-Lógica_de_programação-FFD43B?style=for-the-badge&logoColor=black)
![Status](https://img.shields.io/badge/Status-Em_aprendizado-238636?style=for-the-badge)

Repositório de estudos de Luiz, com exercícios de Python organizados por mundos do Curso em Vídeo.

[Aprendizados](#aprendizados) · [Exercícios em destaque](#exercícios-em-destaque) · [Como executar](#como-executar) · [Próximos passos](#próximos-passos)

</div>

---

## Sobre o projeto

Este espaço registra minha evolução em Python por meio de aulas, desafios e experimentos no terminal. O objetivo é desenvolver raciocínio lógico, transformar enunciados em algoritmos e ganhar autonomia para resolver problemas com código.

Os arquivos preservam as soluções produzidas durante o aprendizado e podem receber melhorias conforme avanço nos estudos.

## Aprendizados

| Etapa | Conteúdos praticados | Aplicações nos exercícios |
| --- | --- | --- |
| **Mundo 1 · Fundamentos** | Entrada e saída com `input()` e `print()`, tipos de dados, conversões, operadores, manipulação de strings e condições com `if` e `else` | Análise de textos, identificação de números pares, cálculo de tarifas, ano bissexto e verificação de triângulos |
| **Mundo 2 · Controle de fluxo** | Condições com `elif`, laços `for` e `while`, `range()`, contadores, acumuladores, `break` e formatação de saída | Jogos no terminal, tabuada, números primos, palíndromos, fatorial, progressão aritmética, Fibonacci e simulação de caixa eletrônico |
| **Mundo 3 · Tuplas** | Indexação, fatiamento, iteração, busca, contagem e uso de `sorted()`, `min()` e `max()` | Números por extenso, classificação de times, sorteios, tabela de preços e identificação de vogais |
| **Mundo 3 · Listas** | Criação e cópia por fatiamento, `append()`, `insert()`, `pop()`, `remove()`, `sort()`, `len()`, `enumerate()` e verificação com `in` e `not in` | Maior e menor valor com suas posições, cadastro sem duplicatas, inserção ordenada, análise de valores e separação de pares e ímpares |

Também pratico o uso dos módulos `random`, `time` e `datetime`, além de saídas formatadas com `.format()` e f-strings.

**Etapa atual:** estudo de listas na aula 17, com soluções desenvolvidas para os desafios 78 a 82. O Mundo 3 reúne os desafios 72 a 82, abrangendo tuplas e listas.

## Exercícios em destaque

| Exercício | O que ele trabalha | Código |
| --- | --- | --- |
| Pedra, papel e tesoura | Condições e sorteio da jogada do computador | [Desafio 45](Mundo%202/a12-e45.py) |
| Verificador de palíndromos | Manipulação de strings e repetição | [Desafio 53](Mundo%202/a13-e53.py) |
| Sequência de Fibonacci | Atualização de valores em um laço | [Desafio 63](Mundo%202/a14-e63.py) |
| Caixa eletrônico | Repetição e cálculo da quantidade de cédulas | [Desafio 71](Mundo%202/a15-e71.py) |
| Números por extenso | Consulta em uma tupla e validação de números entre 0 e 20 | [Desafio 72](mundo%203/a16-e72.py) |
| Classificação de times | Fatiamento, ordenação alfabética com `sorted()` e busca com `index()` | [Desafio 73](mundo%203/a16-e73.py) |
| Maior e menor valor sorteado | Sorteio de números em uma tupla e uso de `max()` e `min()` | [Desafio 74](mundo%203/a16-e74.py) |
| Análise de valores em uma tupla | Contagem, busca e identificação de pares | [Desafio 75](mundo%203/a16-e75.py) |
| Tabela de preços | Percurso de uma tupla e formatação no terminal | [Desafio 76](mundo%203/a16-e76.py) |
| Vogais nas palavras | Laços aninhados e análise de texto | [Desafio 77](mundo%203/a16-e77.py) |
| Maior e menor valor em uma lista | Comparação de valores e identificação de todas as posições com `enumerate()` | [Desafio 78](mundo%203/a17-e78.py) |
| Cadastro de valores sem duplicatas | Verificação com `not in` e inclusão com `append()` | [Desafio 79](mundo%203/a17-e79.py) |
| Inserção em ordem crescente | Uso de `insert()` para manter a lista ordenada durante a entrada | [Desafio 80](mundo%203/a17-e80.py) |
| Análise de valores em uma lista | Contagem, ordenação decrescente e busca pelo valor 5 | [Desafio 81](mundo%203/a17-e81.py) |
| Separação de pares e ímpares | Percurso e distribuição de valores em listas | [Desafio 82](mundo%203/a17-e82.py) |

## Organização

```text
python/
├── README.md
├── mundo 1/               # Fundamentos e primeiras condições
├── Mundo 2/               # Condições e estruturas de repetição
└── mundo 3/               # Tuplas e listas
```

Nos Mundos 2 e 3, nomes como `a16-e75.py` indicam a **aula 16** e o **exercício 75**. Arquivos como `teste.py` reúnem experimentos de estudo.

## Como executar

É necessário ter o **Python 3** instalado. Cada exercício é um script independente, executado pelo terminal a partir da pasta `python`, onde está este README:

```bash
python "Mundo 2/a12-e45.py"
```

Outro exemplo, com tuplas:

```bash
python "mundo 3/a16-e76.py"
```

Para executar um exercício com listas:

```bash
python "mundo 3/a17-e82.py"
```

No Windows, também é possível usar `py` no lugar de `python`. Mantenha as aspas nos caminhos, pois as pastas possuem espaços. Nos exercícios interativos, siga as perguntas apresentadas no terminal.

A maioria dos scripts utiliza apenas recursos do Python e sua biblioteca padrão. O arquivo `mundo 1/a29.py` importa a biblioteca externa `colorama`; para executá-lo, instale-a no ambiente utilizado:

```bash
python -m pip install colorama
```

## Próximos passos

- [x] Praticar fundamentos, strings e operadores.
- [x] Resolver desafios com condições e estruturas de repetição.
- [x] Explorar tuplas em exercícios de análise e apresentação de dados.
- [x] Estudar operações com listas e desenvolver os desafios 78 a 82 da aula 17.
- [ ] Criar e desenvolver o desafio 83 da aula 17.
- [ ] Revisar soluções anteriores com os novos conhecimentos.

---

<div align="center">

**Desenvolvido por Luiz durante seus estudos de Python.**

Material de estudo: Curso em Vídeo · Exercícios e anotações de aprendizado.

</div>
