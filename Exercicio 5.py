# Programa para calcular média de um aluno

# input() pede dados ao usuário
# float() converte o valor digitado para número decimal
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calculando a média
# Soma das notas dividida por 3
media = (nota1 + nota2 + nota3) / 3

# Exibindo a média (com 2 casas decimais)
print(f"\nMédia: {media:.2f}")

# Verificando se o aluno foi aprovado ou reprovado
# Se média maior ou igual a 7 → aprovado
if media >= 7:
    print("Situação: Aprovado ✅")
else:
    print("Situação: Reprovado ❌")