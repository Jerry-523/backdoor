import socket

ip = input("Insira o endereco IP: " )
port = input("Insira a porta: ")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (ip,port)
    sock.bind(address)
    sock.listen(1)
    print("Listening for connection on port:"+ str(port))

    conn , ipvictim = sock.accept()
    msg = "Access guaranted"
    conn.send(msg.encode())
    

main()
