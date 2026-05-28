import pandas as pd

# 1. Carregar os dados
df = pd.read_csv("dados_clientes.csv")

# 2. Média de idade e renda
media_idade = df["Idade"].mean()
media_renda = df["Renda"].mean()

print(f"Média de idade: {media_idade:.2f}")
print(f"Média de renda: R$ {media_renda:.2f}")

# 3. Cidade com mais clientes
cidade_mais_clientes = df["Cidade"].value_counts().idxmax()
print(f"Cidade com mais clientes: {cidade_mais_clientes}")

# 4. Filtrar clientes com renda acima de um valor
valor = float(input("Digite o valor de renda para filtro: "))

clientes_filtrados = df[df["Renda"] > valor]

print("\nClientes com renda acima do valor:")
print(clientes_filtrados)