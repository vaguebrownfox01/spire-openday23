import socket
import time

HEADERSIZE = 5
SERVER_IP = "192.168.1.138"
PORT = 12345
NAME = "pp"

print("Client...")

soc = None


def get_socket(ip=SERVER_IP, port=PORT, name=NAME):
    global soc

    soc = socket.socket()
    host = socket.gethostname()
    name = socket.gethostbyname(host)

    print(f"HOST: {host}, IP: {name}")

    soc.connect((ip, port))

    print("Connected...\n")

    soc.send(name.encode())

    return soc


def get_value(header_size=HEADERSIZE):
    global soc

    message = soc.recv(1024)
    msglen = int(message[:HEADERSIZE])
    message = message.decode("utf-8")

    print("this is message: ", message)

    if message == "":
        print("empty message", message)
        return -1

    if not len(message) - header_size == msglen:
        print("error in message!")
        return -1

    message = message.split()[-1]
    value = int(message)

    return value