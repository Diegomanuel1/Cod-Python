contatos = {}

# Loop principal (menu)
while True:
    print("\n--- Agenda de Contatos ---")
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("4 - Sair")

    # Usuário escolhe uma opção
    opcao = input("Escolha uma opção: ")

    # 1 - Adicionar contato
    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")

        # Salvando no dicionário
        contatos[nome] = {
            "telefone": telefone,
            "email": email
        }

        print("Contato adicionado com sucesso!")

    # 2 - Buscar contato
    elif opcao == "2":
        nome = input("Digite o nome do contato: ")

        # Verifica se o contato existe
        if nome in contatos:
            print("\nContato encontrado:")
            print("Nome:", nome)
            print("Telefone:", contatos[nome]["telefone"])
            print("E-mail:", contatos[nome]["email"])
        else:
            print("Contato não encontrado.")

    # 3 - Listar todos os contatos
    elif opcao == "3":
        # Verifica se há contatos cadastrados
        if len(contatos) == 0:
            print("Nenhum contato cadastrado.")
        else:
            print("\nLista de contatos:")
            
            # Percorre o dicionário
            for nome, dados in contatos.items():
                print(f"\nNome: {nome}")
                print("Telefone:", dados["telefone"])
                print("E-mail:", dados["email"])

    # 4 - Sair
    elif opcao == "4":
        print("Encerrando o programa...")
        break

    # Caso opção inválida
    else:
        print("Opção inválida. Tente novamente.")