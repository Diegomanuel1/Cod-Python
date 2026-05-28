# Criamos uma lista vazia para armazenar os itens
lista_compras = []

# Loop infinito para manter o programa rodando até o usuário decidir sair
while True:
    # Exibindo o menu de opções
    print("\n--- Lista de Compras ---")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Visualizar lista")
    print("4 - Sair")

    # input() para escolher uma opção
    opcao = input("Escolha uma opção: ")

    # Opção 1: Adicionar item
    if opcao == "1":
        item = input("Digite o nome do item: ")
        
        # append() adiciona o item no final da lista
        lista_compras.append(item)
        
        print(f"{item} foi adicionado à lista.")

    # Opção 2: Remover item
    elif opcao == "2":
        item = input("Digite o nome do item a remover: ")
        
        # Verificamos se o item existe na lista
        if item in lista_compras:
            lista_compras.remove(item)  # remove() remove o item da lista
            print(f"{item} foi removido da lista.")
        else:
            print("Item não encontrado na lista.")

    # Opção 3: Visualizar lista
    elif opcao == "3":
        print("\nSua lista de compras:")
        
        # Verifica se a lista está vazia
        if len(lista_compras) == 0:
            print("A lista está vazia.")
        else:
            # for percorre cada item da lista
            for i, item in enumerate(lista_compras, start=1):
                # enumerate() mostra o índice (posição) e o item
                print(f"{i}. {item}")

    # Opção 4: Sair do programa
    elif opcao == "4":
        print("Encerrando o programa...")
        break  # break encerra o loop

    # Caso o usuário digite uma opção inválida
    else:
        print("Opção inválida. Tente novamente.")