import socket
import time

from pong import SERVER_IP, PORT, NAME

# global socket instance
soc = None


def get_socket(ip=SERVER_IP, port=PORT, name=NAME):
    global soc

    soc = socket.socket()
    host = socket.gethostname()
    name = socket.gethostbyname(host)

    print(f"HOST: {host}, IP: {name}")

    # connect
    soc.connect((ip, port))

    print("Connected...\n")

    soc.send(name.encode())


def get_peaks_value():
    global soc

    message = soc.recv(1024)

    # print(message)

    message = message.decode("utf-8")

    # print("this is message: ", message)

    if message == "":
        print("empty message", message)
        return -1

    value = int(message)

    return value

if __name__ == "__main__":
    get_socket()

    while True:
        value = get_peaks_value()
        print('*' * value)