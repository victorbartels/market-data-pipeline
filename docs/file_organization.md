# Organização de arquivos

## Objetivo

Definir a estrutura padrão de armazenamento de arquivos brutos do projeto.

---

# Landing Zone

A landing zone armazena os dados brutos recebidos das APIs públicas sem transformação.

Esses arquivos servem para:

- rastreabilidade
- reprocessamento
- auditoria
- histórico de ingestão

---

# Estrutura adotada

data/landing/{source}/{entity}/{symbol}/{file}.json

---

# Exemplo

data/landing/alpha_vantage/stock_daily/AAPL/AAPL_20260419_213000.json

---

# Convenções

## source

Nome da origem do dado.

Exemplo:
- alpha_vantage
- bcb
- fred

---

## entity

Tipo de dado armazenado.

Exemplo:
- stock_daily
- forex_daily
- macro_series

---

## symbol

Identificador do ativo.

Exemplo:
- AAPL
- MSFT
- PETR4

---

# Objetivo da organização

A estrutura foi definida para permitir:

- escalabilidade
- separação por fonte
- separação por entidade
- histórico de arquivos
- ingestões futuras de múltiplos ativos