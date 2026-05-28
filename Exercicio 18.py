# ============================================
# Importando a biblioteca matplotlib
# ============================================

# pyplot é usado para criar gráficos
import matplotlib.pyplot as plt

# ============================================
# Dados de exemplo
# ============================================

# Lista contendo os nomes das cidades
cidades = [
    "Salvador",
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Recife"
]

# Lista contendo a quantidade de clientes por cidade
quantidade_clientes = [15, 30, 20, 10, 12]

# ============================================
# Criando o gráfico de barras
# ============================================

# Define o tamanho da figura do gráfico
plt.figure(figsize=(10, 5))

# Cria o gráfico de barras
# cidades -> eixo X
# quantidade_clientes -> eixo Y
# color -> define a cor das barras
plt.bar(cidades, quantidade_clientes, color="skyblue")

# ============================================
# Personalizando o gráfico
# ============================================

# Título principal do gráfico
plt.title("Distribuição de Clientes por Cidade")

# Nome do eixo X
plt.xlabel("Cidades")

# Nome do eixo Y
plt.ylabel("Quantidade de Clientes")

# Adiciona uma grade horizontal ao gráfico
plt.grid(axis="y", linestyle="--", alpha=0.7)

# ============================================
# Exibindo os valores acima das barras
# ============================================

# Percorre cada barra para mostrar o valor
for i, valor in enumerate(quantidade_clientes):

    # Coloca o texto acima da barra
    plt.text(i, valor + 0.5, str(valor), ha="center")

# ============================================
# Exibindo o gráfico
# ============================================

# Mostra o gráfico na tela
plt.show()