# Importando o módulo datetime para trabalhar com data e hora
from datetime import datetime


# Função para registrar uma mensagem de log
def registrar_log(tipo, mensagem):
    # datetime.now() pega a data e hora atual
    agora = datetime.now()
    
    # strftime() formata a data/hora em uma string legível
    timestamp = agora.strftime("%Y-%m-%d %H:%M:%S")
    
    # Montando a mensagem final do log
    # Exemplo: [2026-04-30 14:30:00] INFO: Sistema iniciado
    log = f"[{timestamp}] {tipo.upper()}: {mensagem}\n"
    
    # Abrindo o arquivo em modo "append" (a)
    # Isso evita apagar logs antigos
    with open("logs.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(log)  # Escreve a mensagem no arquivo


# Programa principal

# Registrando alguns logs de exemplo
registrar_log("info", "Sistema iniciado")
registrar_log("warning", "Uso de memória alto")
registrar_log("error", "Falha ao conectar ao banco de dados")

print("Logs registrados com sucesso no arquivo 'logs.txt'.")