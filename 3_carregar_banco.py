import pandas as pd
import sqlite3

# Carregar dados tratados
df = pd.read_csv("vendas_tratado.csv")

# Conectar ao banco (cria o arquivo se não existir)
conn = sqlite3.connect("vendas.db")

# Carregar para o banco
df.to_sql("vendas", conn, if_exists="replace", index=False)

print("Dados carregados no banco vendas.db!")
print(f"   Total de registros: {len(df)}")

conn.close()
