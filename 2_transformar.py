import pandas as pd

# Carregar dados brutos
df = pd.read_csv("vendas_raw.csv")

print("=== ANTES DA LIMPEZA ===")
print(df.dtypes)
print(df.isnull().sum())

# 1. Corrigir tipos
df["data"]       = pd.to_datetime(df["data"])
df["quantidade"] = df["quantidade"].astype(int)
df["preco"]      = df["preco"].astype(float)

# 2. Criar colunas novas
df["total"] = df["quantidade"] * df["preco"]
df["mes"]   = df["data"].dt.month
df["ano"]   = df["data"].dt.year

# 3. Remover duplicatas (se houver)
df = df.drop_duplicates()

# 4. Padronizar texto
df["produto"]  = df["produto"].str.strip().str.title()
df["vendedor"] = df["vendedor"].str.strip().str.title()

print("\n=== DEPOIS DA LIMPEZA ===")
print(df.dtypes)
print(df.head())

# Salvar dados tratados
df.to_csv("vendas_tratado.csv", index=False)
print("\n✅ Arquivo vendas_tratado.csv salvo com sucesso!")
