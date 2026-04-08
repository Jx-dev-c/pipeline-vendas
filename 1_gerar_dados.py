import pandas as pd
import random
from datetime import datetime, timedelta

# Configuração
random.seed(42)

produtos = ["Caneta", "Lápis", "Borracha", "Régua", "Caderno"]
vendedores = ["Ana", "Marcos", "Clara", "Luís", "Mariana"]

# Gerar 100 vendas aleatórias
dados = []
data_inicio = datetime(2024, 1, 1)

for i in range(100):
    produto   = random.choice(produtos)
    vendedor  = random.choice(vendedores)
    quantidade = random.randint(1, 20)
    preco      = round(random.uniform(1.50, 50.00), 2)
    data       = data_inicio + timedelta(days=random.randint(0, 364))

    dados.append({
        "id":         i + 1,
        "produto":    produto,
        "vendedor":   vendedor,
        "quantidade": quantidade,
        "preco":      preco,
        "data":       data.strftime("%Y-%m-%d")
    })

df = pd.DataFrame(dados)
df.to_csv("vendas_raw.csv", index=False)

print("✅ Arquivo vendas_raw.csv gerado com sucesso!")
print(df.head())
