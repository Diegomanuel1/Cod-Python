import random  # Para escolher uma palavra aleatória


# Classe responsável por gerenciar a palavra do jogo
class Palavra:
    def __init__(self, lista_palavras):
        # Escolhe uma palavra aleatória da lista
        self.palavra = random.choice(lista_palavras).lower()
        
        # Lista para armazenar letras já descobertas (inicialmente vazia)
        self.letras_descobertas = ["_"] * len(self.palavra)

    def verificar_letra(self, letra):
        # Verifica se a letra está na palavra
        encontrou = False
        
        for i, l in enumerate(self.palavra):
            # Se a letra existir, revela na posição correta
            if l == letra:
                self.letras_descobertas[i] = letra
                encontrou = True
        
        return encontrou

    def palavra_completa(self):
        # Verifica se o jogador já descobriu toda a palavra
        return "_" not in self.letras_descobertas

    def mostrar(self):
        # Retorna a palavra no formato atual (ex: _ a _ a)
        return " ".join(self.letras_descobertas)


# Classe que representa o jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.tentativas = 6  # Número máximo de erros permitidos
        self.letras_tentadas = []  # Armazena letras já usadas

    def tentar_letra(self, letra):
        # Adiciona a letra às tentativas já feitas
        if letra not in self.letras_tentadas:
            self.letras_tentadas.append(letra)
            return True
        else:
            print("Você já tentou essa letra!")
            return False


# Classe principal que controla o jogo
class Jogo:
    def __init__(self):
        # Lista de palavras possíveis
        palavras = ["python", "computador", "programacao", "desenvolvimento"]
        
        # Cria objeto Palavra
        self.palavra = Palavra(palavras)
        
        # Cria o jogador
        nome = input("Digite seu nome: ")
        self.jogador = Jogador(nome)

    def jogar(self):
        print("\n=== Jogo da Forca ===")

        # Loop principal do jogo
        while self.jogador.tentativas > 0:
            # Mostra estado atual da palavra
            print("\nPalavra:", self.palavra.mostrar())
            print("Tentativas restantes:", self.jogador.tentativas)
            print("Letras tentadas:", ", ".join(self.jogador.letras_tentadas))

            # Pede uma letra ao jogador
            letra = input("Digite uma letra: ").lower()

            # Verifica se a letra já foi tentada
            if not self.jogador.tentar_letra(letra):
                continue

            # Verifica se a letra está na palavra
            if self.palavra.verificar_letra(letra):
                print("Boa! Letra correta.")
            else:
                print("Letra incorreta!")
                self.jogador.tentativas -= 1

            # Verifica se o jogador ganhou
            if self.palavra.palavra_completa():
                print("\nParabéns,", self.jogador.nome, "você venceu!")
                print("A palavra era:", self.palavra.palavra)
                break

        # Se acabar as tentativas, o jogador perde
        if self.jogador.tentativas == 0:
            print("\nVocê perdeu!")
            print("A palavra era:", self.palavra.palavra)


# Executando o jogo
if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()