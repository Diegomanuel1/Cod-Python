try:
    # Solicita o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo (ex: texto.txt): ")

    # Abre e lê o arquivo
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("\nConteúdo do arquivo:\n")
        print(conteudo)

# Tratamento de erro
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")