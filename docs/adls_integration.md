# Integração com Azure Data Lake Storage Gen2

## Objetivo

O projeto utiliza o Azure Data Lake Storage Gen2 como landing zone em cloud para armazenar os arquivos brutos extraídos da Alpha Vantage.

## Fluxo atual

Alpha Vantage API → Landing local → ADLS landing container

## Estrutura no ADLS

landing/
└── alpha_vantage/
    └── stock_daily/
        └── AAPL/
            └── arquivo.json

## Segurança

As credenciais do Azure são armazenadas localmente no arquivo `.env` e não devem ser versionadas no GitHub.

## Variáveis utilizadas

- AZURE_STORAGE_ACCOUNT
- AZURE_STORAGE_KEY