# Importando a biblioteca pandas
import pandas as pd

# 1. Carregar os dados do arquivo CSV em um DataFrame
# O arquivo deve estar na mesma pasta do script ou informar o caminho completo
df = pd.read_csv("dados_clientes.csv")

# Exibindo os primeiros dados para conferir se carregou corretamente
print("Visualização inicial dos dados:")
print(df.head())


# 2. Calcular a média de idade e renda dos clientes

# mean() calcula a média de uma coluna numérica
media_idade = df["Idade"].mean()
media_renda = df["Renda"].mean()

print("\nMédia de idade:", media_idade)
print("Média de renda:", media_renda)


# 3. Encontrar a cidade com o maior número de clientes

# value_counts() conta quantas vezes cada valor aparece
contagem_cidades = df["Cidade"].value_counts()

# idxmax() retorna o valor (cidade) com maior frequência
cidade_mais_clientes = contagem_cidades.idxmax()

print("\nCidade com mais clientes:", cidade_mais_clientes)


# 4. Filtrar clientes com renda acima de um valor específico

# Definindo um valor mínimo de renda
valor_minimo = float(input("\nDigite o valor mínimo de renda para filtrar: "))

# Filtrando o DataFrame
# df["Renda"] > valor_minimo cria uma condição (True/False)
clientes_filtrados = df[df["Renda"] > valor_minimo]

print("\nClientes com renda acima de", valor_minimo)
print(clientes_filtrados)