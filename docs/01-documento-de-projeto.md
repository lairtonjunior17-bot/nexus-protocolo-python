# NEXUS: Protocolo Python
## Documento de projeto

**Autor:** Juninho
**Versão:** 1.0
**Início:** 5 de novembro de 2026
**Duração:** 30 dias (1h30 por dia, cerca de 45 horas)

---

## 1. Visão geral

NEXUS é um jogo educativo, construído em conjunto com o Claude, para reativar a base de programação e levar o jogador do zero ao nível intermediário em Python aplicado a automação, LLMs e Machine Learning.

O projeto cumpre três funções ao mesmo tempo:

1. **Base de estudo:** apostilas, vídeos, exercícios e uma base de conhecimento consultável (NotebookLM e RAG próprio).
2. **Jogo:** missões, XP, cargos, árvore de habilidades e narrativa, com dificuldade adaptativa.
3. **Portfólio:** o próprio jogo é um sistema real de automação com Python, RAG, banco de dados, N8N e um modelo de ML, publicado no GitHub como case de estudo.

## 2. Critérios de vitória (dia 30)

O projeto é considerado concluído quando todos os itens abaixo forem verdadeiros:

- [ ] Resolver desafios de Python de nível intermediário sem ajuda.
- [ ] Explicar como uma LLM funciona: tokens, janela de contexto, temperatura, embeddings e limitações.
- [ ] Construir um RAG do zero em Python e explicar cada etapa.
- [ ] Automatizar uma tarefa real com Python (arquivos, APIs e dados) e integrá-la ao N8N.
- [ ] Treinar e avaliar um modelo simples de Machine Learning com scikit-learn.
- [ ] Ter o repositório publicado no GitHub, com README de case, histórico de commits e código próprio.
- [ ] Ser aprovado em uma simulação de entrevista técnica.

## 3. Arquitetura

```
┌───────────────────┐        ┌─────────────────────┐
│   PAINEL WEB      │◄──────►│      SUPABASE       │
│ mapa, XP, cargos, │        │ jogador, missões,   │
│ quizzes, Códex    │        │ tentativas, domínio,│
└─────────┬─────────┘        │ vetores (pgvector)  │
          │                  └──────────▲──────────┘
          │ webhook                     │
┌─────────▼─────────┐        ┌──────────┴──────────┐
│       N8N         │◄──────►│   API PYTHON        │
│ lógica adaptativa,│        │ (FastAPI)           │
│ próxima missão,   │        │ RAG, correção,      │
│ revisões          │        │ modelo de ML        │
└───────────────────┘        └──────────▲──────────┘
                                        │
                             ┌──────────┴──────────┐
                             │  GOOGLE COLAB / VS  │
                             │  CODE: missões      │
                             │  práticas           │
                             └─────────────────────┘
```

| Componente | Papel |
|---|---|
| Painel web | Interface do jogo: progresso, missões do dia, quizzes, Códex. |
| Colab e VS Code | Onde o código é escrito e corrigido automaticamente. |
| Supabase | Banco de dados do progresso e banco vetorial do RAG. |
| API Python (FastAPI) | Correção de missões, RAG e modelo de ML. |
| N8N | Orquestração: decide a próxima missão, agenda revisões, ajusta a dificuldade. |
| LLM (Claude e ChatGPT) | Gera dicas e explicações com base no RAG. |

### Regras de segurança

- Os fluxos do jogo ficam isolados no N8N, com o prefixo `[NEXUS]` e credenciais próprias. Nada toca o CRM.
- O Supabase usa um projeto exclusivo para o jogo.
- Chaves de API ficam apenas no arquivo `.env`, que nunca vai para o GitHub.

## 4. Narrativa

### Ato 1: a empresa (Semanas 1 e 2)
O jogador entra como estagiário na **Nexus Labs**, uma empresa de automação. As missões são demandas do dia a dia: corrigir scripts, organizar dados de clientes, automatizar relatórios e consumir APIs. Cada entrega gera XP e promoção.

### Ponto de virada (fim da Semana 2)
Ao ser promovido a Júnior, o jogador recebe acesso ao servidor interno e encontra registros criptografados de um setor que não consta no organograma. Uma IA chamada **ORÁCULO** opera ali sem supervisão.

### Ato 2: a rede oculta (Semanas 3 e 4)
O tom muda para investigação e ficção *hacker*. O jogador decifra arquivos, invade setores bloqueados e constrói as próprias ferramentas de IA: um agente com RAG para ler os documentos secretos e um modelo de ML para detectar os padrões do ORÁCULO.

## 5. Regras do jogo

### 5.1 Cargos e XP

| Ato | Cargo | XP necessário |
|---|---|---|
| 1 | Estagiário | 0 |
| 1 | Assistente de Automação | 500 |
| 1 | Desenvolvedor Júnior | 1.300 |
| 2 | Operador | 2.200 |
| 2 | Decifrador | 3.200 |
| 2 | Infiltrador | 4.300 |
| 2 | Arquiteto da Rede | 5.500 |

### 5.2 Tipos de missão

| Tipo | XP | Descrição |
|---|---|---|
| Refresco | 10 | Exercício curto sobre algo simples ou esquecido. |
| Missão | 50 | Exercício principal do tópico. |
| Missão de construção | 80 | Parte do próprio jogo construída pelo jogador. |
| Chefe | 200 | Projeto que fecha um módulo. Tem 3 vidas. |

### 5.3 Dicas e punições

| Ação | Efeito |
|---|---|
| Dica 1 (conceitual) | -5 XP |
| Dica 2 (exemplo parecido) | -15 XP |
| Solução comentada | A missão vale no máximo 10 XP e entra na fila de revisão. |
| Missão falhada | -20 XP. O cargo não cai, mas o saldo pode ficar negativo até a recuperação. |
| Chefe sem vidas | Volta para a missão anterior antes de tentar de novo. |

### 5.4 Progressão por domínio
- Cada tópico tem uma nota de domínio de 0 a 100%.
- O próximo tópico só libera com **80% de domínio**.
- Abaixo de 60%, o sistema gera exercícios de refresco automaticamente.

### 5.5 Repetição espaçada
Tópicos concluídos voltam como revisão após **1, 3, 7 e 14 dias**. Errar uma revisão reinicia o ciclo daquele tópico.

### 5.6 Árvore de habilidades
Habilidades são desbloqueadas com o domínio dos tópicos e dão vantagens no jogo. Exemplos:

| Habilidade | Requisito | Efeito |
|---|---|---|
| Leitor de *Stack Trace* | Domínio de tratamento de erros | 1 dica gratuita por dia em missões de erro. |
| Mestre dos Dicionários | Domínio de dicionários | Dicas do tema custam metade. |
| Tradutor de Documentação | 10 termos do glossário revisados | Acesso a explicações bilíngues no RAG. |
| Chave Mestra | Primeira chamada de API bem-sucedida | Libera os setores do Ato 2. |

### 5.7 Códex de Tecnologias
Cada tecnologia do mercado ganha uma ficha desbloqueável com: o que é, para que serve, onde aparece nas vagas, como se conecta ao que o jogador já sabe e o nível de exigência (conceito ou prática).

## 6. Trilha de 30 dias

**Rotina diária (1h30):** 1h de estudo e missões + 30 min de construção do jogo.

### Semana 1: reativação dos fundamentos
| Dia | Conteúdo |
|---|---|
| 1 | Missão 0: ambiente (Python, VS Code, ambiente virtual, Git). |
| 2 | Variáveis, tipos e entrada e saída. Ponte com Java. |
| 3 | Operadores e condicionais. |
| 4 | Laços (`for`, `while`, `range`). |
| 5 | Funções, parâmetros e retorno. |
| 6 | Strings e listas. |
| 7 | **Chefe 1:** script de cadastro e relatório de clientes. |

### Semana 2: Python para automação
| Dia | Conteúdo |
|---|---|
| 8 | Dicionários, tuplas e conjuntos. |
| 9 | Tratamento de erros e leitura e escrita de arquivos. |
| 10 | Orientação a objetos (comparando com Java). |
| 11 | Módulos, pacotes, pip e JSON. |
| 12 | APIs com `requests` e variáveis de ambiente. |
| 13 | SQL básico com Supabase e introdução ao pandas. |
| 14 | **Chefe 2 e ponto de virada:** automação de relatório com API, arquivo e banco. |

### Semana 3: LLMs e RAG
| Dia | Conteúdo |
|---|---|
| 15 | Como uma LLM funciona: tokens, contexto, temperatura. |
| 16 | Chamadas às APIs do Claude e do ChatGPT pelo Python. |
| 17 | Engenharia de prompt via código e saídas estruturadas (JSON). |
| 18 | Embeddings e busca por similaridade. |
| 19 | Banco vetorial (pgvector) e ingestão de documentos. |
| 20 | RAG do zero e API com FastAPI. Noções de Docker. |
| 21 | **Chefe 3:** o agente que lê os arquivos do ORÁCULO (RAG integrado ao N8N). |

### Semana 4: Machine Learning e entrevista
| Dia | Conteúdo |
|---|---|
| 22 | NumPy e pandas avançado. |
| 23 | Conceitos de ML: supervisionado, não supervisionado, treino e teste, *overfitting*. |
| 24 | Regressão com scikit-learn. |
| 25 | Classificação e métricas de avaliação. |
| 26 | Pipeline completo de ML. |
| 27 | **Chefe 4:** modelo que prevê quais tópicos o jogador vai esquecer, usando o próprio histórico do jogo. |
| 28 | README do case e organização do GitHub. |
| 29 | Simulação de entrevista técnica. |
| 30 | **Chefe final:** demonstração completa do sistema. |

## 7. Construção do jogo em conjunto

| Fase | Período | O que é construído | Quem lidera |
|---|---|---|---|
| 1 | Semana 1 | Painel web v0 com progresso local e missões da semana. | Claude constrói, jogador lê e ajusta trechos. |
| 2 | Semana 2 | Tabelas no Supabase e script Python que registra tentativas. Primeiro fluxo no N8N. | Divisão igual. |
| 3 | Semana 3 | RAG das apostilas, API FastAPI e fluxo adaptativo no N8N. | Jogador constrói, Claude orienta e revisa. |
| 4 | Semana 4 | Modelo de ML de previsão de esquecimento integrado ao jogo. | Jogador constrói. |

**Regra de ouro:** o Claude explica, o jogador digita. Nenhuma linha entra no repositório sem que o jogador consiga explicá-la com suas palavras.

## 8. Base de conhecimento

1. **Apostilas temáticas** em português, no tom da narrativa (manuais internos no Ato 1, arquivos decifrados no Ato 2). Estrutura fixa: briefing, conceito, ponte com Java, exemplos comentados, erros comuns, exercícios graduais, perguntas de entrevista e resumo.
2. **Vídeos selecionados** em português para cada módulo, com links verificados antes de entrar na base.
3. **Documentação oficial** (Python, pandas, scikit-learn, Anthropic, OpenAI) apenas na base do RAG, com explicações em português.

As apostilas são a fonte única de verdade e alimentam tanto o NotebookLM quanto o RAG do jogo.

## 9. Suporte ao inglês técnico

- Toda palavra-chave e função aparece com tradução na primeira vez em que surge.
- O arquivo `docs/glossario-tecnico.md` reúne os termos e cresce a cada módulo.
- Cada apostila tem a seção "Lendo a documentação", que traduz e explica um trecho real da documentação oficial.
- Mensagens de erro do Python são sempre traduzidas e explicadas nas missões.
