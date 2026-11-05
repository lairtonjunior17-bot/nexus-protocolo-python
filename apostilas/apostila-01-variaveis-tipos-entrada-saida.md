# Apostila 1: variáveis, tipos, entrada e saída

> **NEXUS LABS · Manual interno do colaborador · Volume 1**
>
> Todo sistema da Nexus Labs começa da mesma forma: receber dados, guardá-los e devolver uma resposta. Este manual explica como o Python faz isso. Leia antes de abrir qualquer arquivo do setor de Cadastro.
>
> *Nota escrita à mão na margem: "o input mente. Sempre confira o tipo." (assinatura ilegível)*

**Tempo de estudo:** 40 minutos · **Missão vinculada:** Missão 1, O cadastro quebrado

---

## 1. O que você vai aprender

1. Criar variáveis e entender como o Python decide o tipo delas.
2. Reconhecer os quatro tipos básicos: `int`, `float`, `str` e `bool`.
3. Receber dados com `input()` e mostrar resultados com `print()`.
4. Converter tipos com `int()`, `float()` e `str()`.
5. Formatar textos com *f-strings*.
6. Ler os três erros mais comuns deste tema: `TypeError`, `ValueError` e `NameError`.

---

## 2. Variáveis

Uma variável é um **nome que aponta para um valor** guardado na memória.

```python
cliente = "Ana"
consumo = 300
tarifa = 0.75
ativo = True
```

O sinal `=` não quer dizer "igual" como na matemática. Ele quer dizer **"guarde este valor neste nome"**. Por isso, isto é válido:

```python
contador = 1
contador = contador + 1   # agora contador vale 2
```

### Ponte com Java

| Java | Python |
|---|---|
| `String cliente = "Ana";` | `cliente = "Ana"` |
| `int consumo = 300;` | `consumo = 300` |
| `double tarifa = 0.75;` | `tarifa = 0.75` |
| `boolean ativo = true;` | `ativo = True` |

Três diferenças importantes:

1. **Não se declara o tipo.** O Python descobre sozinho, olhando para o valor. Isso se chama **tipagem dinâmica**.
2. **Não há ponto e vírgula.** O fim da linha encerra a instrução.
3. **`True` e `False` começam com letra maiúscula.** Escrever `true` gera erro.

### Regras para nomes

- Use letras minúsculas e separe palavras com sublinhado: `consumo_mensal`, e não `consumoMensal`. Esse padrão se chama *snake_case* e é a convenção oficial do Python, definida na PEP 8. Em Java, o padrão é *camelCase*.
- O nome não pode começar com número: `1cliente` é inválido.
- Maiúsculas e minúsculas fazem diferença: `Cliente` e `cliente` são variáveis diferentes.
- Prefira nomes que explicam o conteúdo: `gasto_anual` é melhor do que `g`.

---

## 3. Os quatro tipos básicos

| Tipo | Nome completo | Exemplo | Uso típico |
|---|---|---|---|
| `int` | *integer* (inteiro) | `300`, `-5`, `2026` | Contagens, idades, anos |
| `float` | *floating point* (ponto flutuante) | `0.75`, `250.5` | Valores com casas decimais |
| `str` | *string* (cadeia de caracteres) | `"Ana"`, `'kWh'` | Textos |
| `bool` | *boolean* (lógico) | `True`, `False` | Sim ou não, ligado ou desligado |

Para descobrir o tipo de qualquer valor, use `type()`:

```python
print(type(300))      # <class 'int'>
print(type(0.75))     # <class 'float'>
print(type("Ana"))    # <class 'str'>
print(type(True))     # <class 'bool'>
```

**Atenção:** no Python, o separador decimal é sempre o **ponto**, nunca a vírgula. `0,75` não é um número; para o Python, isso são dois valores separados.

---

## 4. Saída de dados: `print()`

```python
print("Bem-vindo à Nexus Labs")
print("Cliente:", "Ana")          # vírgula separa itens com um espaço
print("Linha 1\nLinha 2")         # \n quebra a linha
```

### *f-strings*: o jeito moderno de montar textos

Coloque um `f` antes das aspas e escreva variáveis entre chaves:

```python
cliente = "Ana"
gasto = 2700
print(f"Cliente {cliente} gastou R$ {gasto} no ano.")
```

Dentro das chaves, também é possível fazer contas e formatar números:

```python
tarifa = 0.7512
print(f"Tarifa: R$ {tarifa:.2f}")        # Tarifa: R$ 0.75
print(f"Consumo anual: {300 * 12} kWh")  # Consumo anual: 3600 kWh
```

O `:.2f` significa "mostre como número decimal (`f`) com 2 casas depois do ponto (`.2`)". Você vai usar isso o tempo todo com valores em dinheiro.

| Java | Python |
|---|---|
| `"Cliente " + nome` | `f"Cliente {nome}"` |
| `String.format("%.2f", valor)` | `f"{valor:.2f}"` |
| `System.out.println(...)` | `print(...)` |

---

## 5. Entrada de dados: `input()`

```python
nome = input("Nome do cliente: ")
```

O `input()` mostra o texto entre parênteses, espera a pessoa digitar e pressionar Enter e devolve o que foi digitado.

### A regra mais importante desta apostila

**O `input()` sempre devolve texto (`str`)**, mesmo quando a pessoa digita um número.

```python
idade = input("Idade: ")    # a pessoa digita 30
print(type(idade))          # <class 'str'>, e não int
print(idade * 2)            # 3030 (o texto repetido duas vezes!)
```

Esta é a "mentira do input" da anotação na capa. Para fazer contas, é preciso **converter**.

---

## 6. Conversão de tipos

| Função | Converte para | Exemplo | Resultado |
|---|---|---|---|
| `int()` | inteiro | `int("30")` | `30` |
| `float()` | decimal | `float("0.75")` | `0.75` |
| `str()` | texto | `str(3600)` | `"3600"` |

O padrão mais comum é converter já na leitura:

```python
idade = int(input("Idade: "))
tarifa = float(input("Tarifa: "))
```

Leia de dentro para fora: primeiro o `input()` recebe o texto, depois o `int()` ou o `float()` converte o resultado.

### Ponte com Java

```java
int idade = Integer.parseInt(scanner.nextLine());
```

```python
idade = int(input())
```

A lógica é a mesma, com bem menos código.

---

## 7. Erros comuns

### `TypeError`: tipos incompatíveis

```python
consumo = 3600
print("Consumo: " + consumo)
```

```
TypeError: can only concatenate str (not "int") to str
```

**Tradução:** "só é possível concatenar (juntar) str com str, e não com int."
**Causa:** o `+` entre texto e número. O Python não converte sozinho.
**Solução:** use `str(consumo)` ou, melhor, uma f-string: `f"Consumo: {consumo}"`.

Outro caso:

```python
consumo = "300"        # veio de um input() sem conversão
print(consumo * 0.75)
```

```
TypeError: can't multiply sequence by non-int of type 'float'
```

**Tradução:** "não é possível multiplicar uma sequência (o texto) por algo que não seja inteiro, do tipo float."
**Causa:** um texto multiplicado por um decimal.

### `ValueError`: valor impossível de converter

```python
int("trezentos")
float("0,75")
```

```
ValueError: invalid literal for int() with base 10: 'trezentos'
```

**Tradução:** "valor literal inválido para int() na base 10."
**Causa:** o texto não representa um número. Lembre-se de que `"0,75"` com vírgula também falha.

### `NameError`: nome inexistente

```python
gasto_anual = 2700
print(gasto_anul)
```

```
NameError: name 'gasto_anul' is not defined. Did you mean: 'gasto_anual'?
```

**Tradução:** "o nome 'gasto_anul' não está definido. Você quis dizer 'gasto_anual'?"
**Causa:** um erro de digitação. As versões recentes do Python chegam a sugerir o nome correto.

---

## 8. Lendo a documentação

Trecho real da documentação oficial da função `input()`:

> *"If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that."*

| Inglês | Português |
|---|---|
| *If the prompt argument is present* | Se o argumento *prompt* (o texto da pergunta) for informado |
| *it is written to standard output* | ele é escrito na saída padrão (a tela) |
| *without a trailing newline* | sem uma quebra de linha no final |
| *reads a line from input* | lê uma linha da entrada (o teclado) |
| *converts it to a string* | converte essa linha em texto |
| *stripping a trailing newline* | removendo a quebra de linha do final |
| *and returns that* | e devolve esse resultado |

Repare na frase *converts it to a string*: a própria documentação confirma a regra da seção 5.

---

## 9. Exercícios de refresco

Responda sem rodar o código, depois confira no terminal. Para testar rapidamente, digite `python` no terminal, que abre o **modo interativo** (o prompt muda para `>>>`). Para sair, digite `exit()`.

1. Qual é o tipo de cada valor? `42`, `"42"`, `42.0`, `False`.
2. O que este código mostra? `print("5" + "5")`
3. E este? `print(int("5") + int("5"))`
4. Corrija: `print("Total: " + 10)`
5. Qual é o problema em `tarifa = float(input("Tarifa: "))` se a pessoa digitar `0,80`?
6. Escreva uma linha que mostre `Valor: R$ 7.50` a partir de `valor = 7.5`.

<details>
<summary>Respostas (abra só depois de tentar)</summary>

1. `int`, `str`, `float` e `bool`.
2. `55`. Somar textos é juntá-los.
3. `10`.
4. `print(f"Total: {10}")` ou `print("Total: " + str(10))`.
5. `ValueError`, porque o Python usa ponto como separador decimal.
6. `print(f"Valor: R$ {valor:.2f}")`.

</details>

---

## 10. Perguntas de entrevista

1. O que significa dizer que o Python tem tipagem dinâmica? Compare com o Java.
2. Qual é o tipo do valor devolvido por `input()`? Que problema isso pode causar?
3. Qual é a diferença entre `TypeError` e `ValueError`?
4. Por que usar f-strings em vez de concatenar com `+`?

---

## 11. Vídeo de apoio

**Curso em Vídeo, Python 3, Mundo 1** (professor Gustavo Guanabara). Pesquise no YouTube por "Curso em Vídeo Python Mundo 1" e assista às aulas sobre **tipos primitivos e saída de dados**. Ao adicionar ao NotebookLM, junte o vídeo e esta apostila na mesma fonte de estudo.

---

## 12. Resumo

- Variável é um nome que aponta para um valor. O tipo é definido pelo valor, e não por uma declaração.
- Os tipos básicos são `int`, `float`, `str` e `bool`. Use `type()` para conferir.
- O `input()` **sempre** devolve `str`. Converta com `int()` ou `float()` antes de fazer contas.
- Use f-strings para montar textos e `:.2f` para valores com duas casas decimais.
- `TypeError`: tipos incompatíveis. `ValueError`: conversão impossível. `NameError`: nome inexistente.
