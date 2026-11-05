# Missão 1: O cadastro quebrado

> **NEXUS LABS · Setor de Cadastro · Demanda nº 0001**
>
> Estagiário, o setor de Energia precisa de duas coisas até o fim do dia.
>
> Primeiro: o estagiário anterior deixou um script que calcularia o consumo anual dos clientes. Ele nunca funcionou. Conserte.
>
> Segundo: precisamos de um script novo, que monte a ficha de um cliente. As especificações estão abaixo. Siga à risca: o sistema de conferência é automático e não aceita variações.
>
> *Coordenação de Automação*

**Estudo prévio:** [Apostila 1](../../apostilas/apostila-01-variaveis-tipos-entrada-saida.md)
**Recompensa:** 50 XP por parte (100 XP no total)

---

## Parte A: consertar o script do estagiário anterior

Arquivo: `cadastro_quebrado.py` (já está nesta pasta).

O script tem **três defeitos**. Corrija o arquivo, sem reescrevê-lo do zero. Quando ele estiver certo, rodar o script e digitar `Ana`, `300` e `0.75` deve mostrar:

```
Cliente: Ana
Consumo anual: 3600 kWh
Gasto anual: R$ 2700.00
```

O consumo mensal deve ser tratado como **número inteiro**.

**Como trabalhar:** rode o script, leia o erro, corrija um defeito e rode de novo. Repita até funcionar.

```bash
python missoes/missao-01-cadastro/cadastro_quebrado.py
```

## Parte B: criar a ficha de cliente

Crie, nesta pasta, o arquivo `cadastro_cliente.py`. Desta vez, você escreve tudo.

**O script deve pedir, nesta ordem:**

1. O nome do cliente (texto).
2. A idade (número inteiro).
3. O valor da conta de energia mensal (número decimal).

**E deve mostrar:**

```
Ficha do cliente: Ana
Idade: 30 anos
Ano de nascimento aproximado: 1996
Conta mensal: R$ 250.50
Gasto anual: R$ 3006.00
```

Regras:

- O ano de nascimento aproximado é `2026 - idade`.
- O gasto anual é a conta mensal multiplicada por 12.
- Os valores em dinheiro aparecem sempre com duas casas decimais.
- Os textos das perguntas do `input()` ficam a seu critério.

---

## Verificação

```bash
python missoes/missao-01-cadastro/verificar_missao_01.py
```

O verificador roda os seus scripts com dados de teste diferentes dos exemplos acima. Ou seja, o código precisa calcular de verdade, e não apenas mostrar os valores do exemplo. Cada parte aprovada registra o XP no painel automaticamente.

Você pode rodar o verificador quantas vezes quiser, sem perder XP.

## Dicas (custam XP)

Tente sozinho primeiro. Se travar, peça uma dica pelo terminal:

```bash
python nucleo/dica.py missao-01 A 1
```

| Comando | Conteúdo | Custo |
|---|---|---|
| `... missao-01 A 1` | Dica conceitual da Parte A | -5 XP |
| `... missao-01 A 2` | Caminho detalhado da Parte A | -15 XP |
| `... missao-01 B 1` | Dica conceitual da Parte B | -5 XP |
| `... missao-01 B 2` | Exemplo parecido para a Parte B | -15 XP |

Cada dica só é cobrada uma vez. Você também pode me perguntar no chat, e a regra é a mesma: me diga qual parte e mostre o erro.

## Entrega

```bash
git add missoes/missao-01-cadastro painel
```

```bash
git commit -m "Missão 1: cadastro corrigido e ficha de cliente"
```

```bash
git push
```

O `painel` entra no commit porque o verificador atualizou o seu progresso.

## Perguntas para responder no chat

1. Quais eram os três defeitos da Parte A, e qual tipo de erro cada um gerava?
2. Por que `"300" * 12` não dá erro, mas também não dá o resultado esperado?
