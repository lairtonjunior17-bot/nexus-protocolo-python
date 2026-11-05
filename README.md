# NEXUS: Protocolo Python

Jogo educativo de aprendizado adaptativo que leva o jogador do zero ao nível intermediário em **Python para automação, LLMs e Machine Learning**, construído em 30 dias como case de estudo e portfólio.

O próprio jogo é um sistema real: painel web, banco de dados no Supabase, orquestração no N8N, RAG sobre uma base de conhecimento própria e um modelo de ML que prevê quais tópicos o jogador tende a esquecer.

## Status

| Fase | Situação |
|---|---|
| Documento de projeto | Concluído |
| Missão 0: ambiente | Em andamento |
| Painel web v0 | A fazer |
| Banco de dados e N8N | A fazer |
| RAG | A fazer |
| Modelo de ML | A fazer |

## Estrutura

```
docs/       documento de projeto e glossário técnico
missoes/    missões práticas com verificadores automáticos
apostilas/  material de estudo temático (fonte do NotebookLM e do RAG)
painel/     interface web do jogo
banco/      esquema e migrações do Supabase
n8n/        fluxos exportados do N8N
rag/        pipeline de ingestão, embeddings e consulta
ml/         modelo de previsão de esquecimento
```

## Documentação

- [Documento de projeto](docs/01-documento-de-projeto.md)
- [Glossário técnico](docs/glossario-tecnico.md)
- [Missão 0: Credenciamento](missoes/missao-00-ambiente/README.md)
