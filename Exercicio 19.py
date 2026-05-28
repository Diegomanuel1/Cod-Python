import requests  # Para fazer requisições HTTP (acessar o site)
from bs4 import BeautifulSoup  # Para analisar o HTML da página

# URL do site de notícias (página principal da BBC)
url = "https://www.bbc.com/news"

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida (status code 200 = OK)
if response.status_code == 200:
    
    # Criando o objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Procurando todas as tags de título de notícia
    # Na BBC, muitos títulos estão em tags <h2>
    titulos = soup.find_all("h2")
    
    # Lista para armazenar os textos dos títulos
    lista_titulos = []
    
    # Percorrendo cada título encontrado
    for titulo in titulos:
        texto = titulo.get_text(strip=True)  # Remove espaços extras
        
        # Evita adicionar títulos vazios
        if texto:
            lista_titulos.append(texto)
    
    # Salvando os títulos em um arquivo de texto
    with open("titulos_noticias.txt", "w", encoding="utf-8") as arquivo:
        
        # Escrevendo cada título em uma nova linha
        for t in lista_titulos:
            arquivo.write(t + "\n")
    
    print("Títulos salvos com sucesso no arquivo 'titulos_noticias.txt'.")

else:
    # Caso a requisição falhe
    print("Erro ao acessar o site:", response.status_code)