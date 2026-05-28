
# input() serve para pedir dados ao usuário pelo teclado
# float() converte o valor digitado (texto) para número decimal
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizando a soma dos dois números
soma = num1 + num2

# Realizando a subtração (primeiro número menos o segundo)
subtracao = num1 - num2

# Realizando a multiplicação
multiplicacao = num1 * num2

# Para a divisão, precisamos verificar se o segundo número é zero
# Isso evita erro no programa (divisão por zero não é permitida)
if num2 != 0:
    divisao = num1 / num2  # Se for diferente de zero, realiza a divisão
else:
    divisao = "Não é possível dividir por zero"  # Mensagem de erro

# Exibindo os resultados na tela
# \n serve para pular uma linha e deixar a saída mais organizada
print("\nResultados:")

# Mostrando o resultado da soma
print("Soma:", soma)

# Mostrando o resultado da subtração
print("Subtração:", subtracao)

# Mostrando o resultado da multiplicação
print("Multiplicação:", multiplicacao)

# Mostrando o resultado da divisão
print("Divisão:", divisao)