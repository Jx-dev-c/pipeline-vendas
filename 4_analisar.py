import sqlite3
import pandas as pd

conn = sqlite3.connect("vendas.db")

# 1. Produto mais vendido (por quantidade)
print("=== PRODUTO MAIS VENDIDO ===")
query1 = """
    SELECT produto,
           SUM(quantidade) AS total_quantidade
    FROM vendas
    GROUP BY produto
    ORDER BY total_quantidade DESC
"""
print(pd.read_sql(query1, conn))

# 2. Receita por mês
print("\n=== RECEITA POR MÊS ===")
query2 = """
    SELECT mes,
           ROUND(SUM(total), 2) AS receita_total
    FROM vendas
    GROUP BY mes
    ORDER BY mes
"""
print(pd.read_sql(query2, conn))

# 3. Top 3 vendedores por receita
print("\n=== TOP 3 VENDEDORES ===")
query3 = """
    SELECT vendedor,
           ROUND(SUM(total), 2) AS receita_total
    FROM vendas
    GROUP BY vendedor
    ORDER BY receita_total DESC
    LIMIT 3
"""
print(pd.read_sql(query3, conn))

# 4. Ticket médio por produto
print("\n=== TICKET MÉDIO POR PRODUTO ===")
query4 = """
    SELECT produto,
           ROUND(AVG(total), 2) AS ticket_medio
    FROM vendas
    GROUP BY produto
    ORDER BY ticket_medio DESC
"""
print(pd.read_sql(query4, conn))

conn.close()
