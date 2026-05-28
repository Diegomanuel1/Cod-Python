# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(c):
    # Fórmula: (C * 9/5) + 32
    return (c * 9/5) + 32

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(f):
    # Fórmula: (F - 32) * 5/9
    return (f - 32) * 5/9


# Programa principal

# Exibe o menu para o usuário escolher o tipo de conversão
print("Conversor de Temperatura")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")

# input() lê a opção escolhida
opcao = input("Escolha uma opção: ")

# Verifica qual opção foi escolhida
if opcao == "1":
    # Solicita a temperatura em Celsius
    c = float(input("Digite a temperatura em Celsius: "))
    
    # Chama a função de conversão
    resultado = celsius_para_fahrenheit(c)
    
    # Exibe o resultado
    print(f"{c}°C equivale a {resultado:.2f}°F")

elif opcao == "2":
    # Solicita a temperatura em Fahrenheit
    f = float(input("Digite a temperatura em Fahrenheit: "))
    
    # Chama a função de conversão
    resultado = fahrenheit_para_celsius(f)
    
    # Exibe o resultado
    print(f"{f}°F equivale a {resultado:.2f}°C")

else:
    # Caso o usuário digite uma opção inválida
    print("Opção inválida. Tente novamente.")