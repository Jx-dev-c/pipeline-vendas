# Pipeline de Vendas — Projeto de Engenharia de Dados

Pipeline ETL simples de vendas usando Python, Pandas e SQL.

## Estrutura do Projeto

```
pipeline_vendas/
│
├── 1_gerar_dados.py      # Gera dados fictícios de vendas (CSV)
├── 2_transformar.py      # Limpa e transforma os dados
├── 3_carregar_banco.py   # Carrega os dados no banco SQLite
├── 4_analisar.py         # Consultas SQL para análise
└── README.md
```

## Como Rodar

Instale as dependências:
```bash
pip install pandas
```

Execute os scripts na ordem:
```bash
python 1_gerar_dados.py
python 2_transformar.py
python 3_carregar_banco.py
python 4_analisar.py
```

## O que o Pipeline Faz

1. **Geração** — cria 100 registros fictícios de vendas com produto, vendedor, quantidade, preço e data
2. **Transformação** — corrige tipos, remove duplicatas, padroniza texto e cria colunas calculadas (`total`, `mes`, `ano`)
3. **Carga** — salva os dados tratados num banco SQLite local
4. **Análise** — responde perguntas de negócio com SQL:
   - Produto mais vendido
   - Receita por mês
   - Top 3 vendedores
   - Ticket médio por produto

## Tecnologias

- Python 3
- Pandas
- SQLite
