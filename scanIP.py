import socket
import sys

# Verifica se o IP foi passado
if len(sys.argv) < 2:
    print(f"Uso: {sys.argv[0]} <IP> [PORTA]")
    sys.exit(1)

target = sys.argv[1]

# Se uma porta específica foi passada, escaneia só ela
if len(sys.argv) == 3:
    try:
        port = int(sys.argv[2])
        print(f" Escaneando {target} na porta {port}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"+ Porta {port} está aberta")
        else:
            print(f"x Porta {port} está fechada")
        s.close()
    except ValueError:
        print("Erro: a porta precisa ser um número inteiro.")
        sys.exit(1)

# Se só o IP foi passado, escaneia todas as portas e retorna abertas
else:
    print(f" Escaneando todas as portas de {target}")
    open_ports = []

    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()

    print("\nPortas abertas encontradas:")
    for port in open_ports:
        print(f"+ Porta {port}")

