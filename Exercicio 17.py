# ============================================
# Classe ContaBancaria
# ============================================
class ContaBancaria:
    """
    Classe responsável por representar uma conta bancária.
    Cada conta possui:
    - número da conta
    - saldo
    - titular
    """

    # Método construtor da classe
    def __init__(self, numero_conta, titular, saldo=0):
        # Número identificador da conta
        self.numero_conta = numero_conta

        # Nome do titular da conta
        self.titular = titular

        # Saldo inicial da conta
        self.saldo = saldo

    # Método para realizar depósito
    def depositar(self, valor):
        """
        Adiciona dinheiro ao saldo da conta.
        """

        # Verifica se o valor é positivo
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    # Método para realizar saque
    def sacar(self, valor):
        """
        Retira dinheiro da conta, se houver saldo suficiente.
        """

        # Verifica se o valor do saque é válido
        if valor <= 0:
            print("O valor do saque deve ser positivo.")

        # Verifica se há saldo suficiente
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")

        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    # Método para consultar saldo
    def verificar_saldo(self):
        """
        Exibe o saldo atual da conta.
        """
        print(f"Saldo atual: R$ {self.saldo:.2f}")


# ============================================
# Classe Cliente
# ============================================
class Cliente:
    """
    Classe responsável por representar um cliente do banco.
    Cada cliente possui:
    - nome
    - cpf
    - lista de contas bancárias
    """

    # Método construtor
    def __init__(self, nome, cpf):
        # Nome do cliente
        self.nome = nome

        # CPF do cliente
        self.cpf = cpf

        # Lista para armazenar as contas do cliente
        self.contas = []

    # Método para adicionar uma conta ao cliente
    def adicionar_conta(self, conta):
        """
        Adiciona uma conta bancária à lista de contas do cliente.
        """
        self.contas.append(conta)
        print(f"Conta {conta.numero_conta} adicionada ao cliente {self.nome}.")


# ============================================
# Classe Banco
# ============================================
class Banco:
    """
    Classe responsável por gerenciar os clientes e contas do banco.
    """

    # Método construtor
    def __init__(self, nome):
        # Nome do banco
        self.nome = nome

        # Lista de clientes cadastrados
        self.clientes = []

    # Método para adicionar um novo cliente
    def adicionar_cliente(self, cliente):
        """
        Adiciona um cliente à lista de clientes do banco.
        """
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado ao banco.")

    # Método para buscar uma conta pelo número
    def buscar_conta(self, numero_conta):
        """
        Procura uma conta bancária em todos os clientes do banco.
        """

        # Percorre todos os clientes
        for cliente in self.clientes:

            # Percorre todas as contas do cliente
            for conta in cliente.contas:

                # Verifica se o número da conta corresponde
                if conta.numero_conta == numero_conta:
                    return conta

        # Caso a conta não seja encontrada
        return None


# ============================================
# Programa principal
# ============================================

# Criando o banco
banco = Banco("Banco Python")

# Criando clientes
cliente1 = Cliente("João Silva", "123.456.789-00")
cliente2 = Cliente("Maria Souza", "987.654.321-00")

# Adicionando clientes ao banco
banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

# Criando contas bancárias
conta1 = ContaBancaria(1001, "João Silva", 500)
conta2 = ContaBancaria(1002, "Maria Souza", 1000)

# Associando contas aos clientes
cliente1.adicionar_conta(conta1)
cliente2.adicionar_conta(conta2)

# ============================================
# Operações bancárias
# ============================================

# Depositando dinheiro
conta1.depositar(200)

# Sacando dinheiro
conta2.sacar(300)

# Consultando saldo
conta1.verificar_saldo()
conta2.verificar_saldo()

# ============================================
# Buscando uma conta no banco
# ============================================

# Busca da conta pelo número
conta_encontrada = banco.buscar_conta(1001)

# Verifica se a conta foi encontrada
if conta_encontrada:
    print("\nConta encontrada!")
    print(f"Titular: {conta_encontrada.titular}")
    conta_encontrada.verificar_saldo()
else:
    print("Conta não encontrada.")