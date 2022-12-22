import socket

ip = input("Insira o endereco IP: ")
port = input("Insira a porta: ")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (ip, int(port))
    sock.connect(address)

    msg = sock.recv(1024)

    print(msg.decode())

    while True:
        msg = input("$ ")
        
        # Fazer padding na mensagem se o comprimento for inferior a 80
        if len(msg) < 80:
            msg = msg + " " * (80 - len(msg))
        sock.send(msg.encode())

        response = sock.recv(80)
        print(response.decode())
main()
