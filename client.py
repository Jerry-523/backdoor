import socket

ip = input("Insira o endereco IP: ")
port = input("Insira a porta: ")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (ip,port)
    sock.connect(address)

    msg = sock.recv(1024)

    print(msg.decode())

    sock.close()

main()
