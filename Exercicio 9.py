# Função recursiva para calcular o fatorial

def fatorial(n):
    # Caso base:
    # O fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    
    # Caso recursivo:
    # n! = n * (n - 1)!
    else:
        return n * fatorial(n - 1)

# Programa principal

# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é negativo
if numero < 0:
    print("Fatorial não existe para números negativos.")
else:
    # Chama a função e mostra o resultado
    resultado = fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")
    