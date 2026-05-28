# Importando módulos necessários
import random  # Para gerar escolhas aleatórias
import string  # Contém conjuntos de caracteres prontos (letras, números, etc.)

# Função para gerar senha
def gerar_senha(tamanho):
    # string.ascii_letters -> letras minúsculas + maiúsculas
    # string.digits -> números (0-9)
    # string.punctuation -> caracteres especiais (!@#$%...)
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # random.choice() escolhe um caractere aleatório
    # O for repete isso 'tamanho' vezes
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))

    return senha


# Programa principal

# Solicita ao usuário o tamanho da senha
tamanho = int(input("Digite o tamanho da senha: "))

# Verifica se o tamanho é válido
if tamanho <= 0:
    print("O tamanho deve ser maior que zero.")
else:
    # Gera a senha
    senha = gerar_senha(tamanho)
    
    # Exibe a senha gerada
    print("Senha gerada:", senha)