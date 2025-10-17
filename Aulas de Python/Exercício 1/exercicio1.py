import pandas as pd
import matplotlib.pyplot as plt

#Exercicio 1
# Criar o DataFrame
dados = pd.DataFrame({
    "Produto": ["Mouse", "Teclado", "Monitor", "Fone", "Cadeira"],
    "Categoria": ["Periféricos", "Periféricos", "Monitores", "Periféricos", "Móveis"],
    "Quantidade": [150, 100, 60, 200, 30],
    "Preço Unitário": [45.90, 99.90, 899.00, 35.00, 450.00],
    "Região": ["Sul", "Sudeste", "Nordeste", "Sul", "Centro-Oeste"]
})

# Salvar como CSV
dados.to_csv("vendas_lojas.csv", index=False)

# === 1. Ler o arquivo CSV ===
dados = pd.read_csv("vendas_lojas.csv")

# === 2. Calcular o total de vendas ===
dados["Total Vendas"] = dados["Quantidade"] * dados["Preço Unitário"]
print("=== Dados com Total de Vendas ===")
print(dados)

# === 3. Categoria que gerou mais receita ===
receita_por_categoria = dados.groupby("Categoria")["Total Vendas"].sum()
categoria_mais_lucrativa = receita_por_categoria.idxmax()
print("\n=== Receita por Categoria ===")
print(receita_por_categoria)
print(f"\nCategoria que gerou mais receita: {categoria_mais_lucrativa}")

# === 4. Gráfico de barras: receita por região ===
receita_por_regiao = dados.groupby("Região")["Total Vendas"].sum()
receita_por_regiao.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Receita por Região")
plt.xlabel("Região")
plt.ylabel("Total de Vendas (R$)")
plt.tight_layout()
plt.show()

# === 5. Produtos com quantidade < 50 ===
poucas_vendas = dados[dados["Quantidade"] < 50]
print("\n=== Produtos com menos de 50 unidades vendidas ===")
print(poucas_vendas)
