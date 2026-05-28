# Função para contar vogais em uma string
def contar_vogais(texto):
    # Definindo as vogais (minúsculas)
    vogais = "aeiou"
    
    # Contador de vogais
    contador = 0

    # Convertendo o texto para minúsculas
    # Isso permite contar tanto 'A' quanto 'a'
    texto = texto.lower()

    # Percorrendo cada caractere da string
    for letra in texto:
        # Verifica se a letra está dentro das vogais
        if letra in vogais:
            contador += 1  # Soma 1 ao contador

    # Retorna o total de vogais encontradas
    return contador


# Programa principal (exemplo de uso)
frase = input("Digite uma palavra ou frase: ")

# Chamando a função
resultado = contar_vogais(frase)

# Exibindo o resultado
print("Número de vogais:", resultado)