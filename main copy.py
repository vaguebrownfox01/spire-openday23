#!/home/pi/openday/opendemo/bin/python

import time, socket
import RPi.GPIO as GPIO
from time import sleep

MOTOR_PIN = 12
GPIO.setwarnings(False)                 #disable warnings
GPIO.setmode(GPIO.BOARD)                #set pin numbering system
GPIO.setup(MOTOR_PIN, GPIO.OUT)

pi_pwm = GPIO.PWM(MOTOR_PIN, 100)               #create PWM instance with frequency
pi_pwm.start(0)

headersize=5

print("Clint server...")
time.sleep(1)
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(f"{shost}, {ip}")
server_host = "192.168.1.138" #input("Enter Server's IP address:")
name = "pp" #input("Enter Client's name:")
port = 12345
print(f"Trying to connect to the server:{server_host},{port}")
time.sleep(1)
soc.connect((server_host, port))
print("Connected...\n")
soc.send(name.encode())
# server_name=soc.recv(1024)
# server_name=server_name.decode()
# print('{} has joined...'.format(server_name))
# print('Enter [bye] to exit.')
# while True:
# max = 0÷

i = 0
MAX_PEAK = 1
BASE_DUTY = 60
speed = lambda x: round((-40 / MAX_PEAK ** 2) * x ** 2 + (80 / MAX_PEAK) * x + BASE_DUTY)
max = 8
while True:
    #message = soc.recv(2)
    #message = message.decode()
    #if not message == "":
        #print(">", message)
        #value = int(message)
        #max = value if value > max else ma
        #pi_pwm.ChangeDutyCycle(value)
        #sleep(0.01)
    message=soc.recv(1024)
    msglen=int(message[:headersize])
    message=message.decode("utf-8")
    if len(message)-headersize==msglen:
        print("full msg received",message)
        message=message.split()
        # print("POST SPLITTING MESSAGE ", message, message[0], message[1])
        # message=message[:-1]
	
        value = int(message[-1])
        max = value if max < value else max

        sleep(0.01)
        MAX_PEAK = max
        if (i%52 == 0):
            max = 16

        i += 1
        n_value = speed(value)
        pi_pwm.ChangeDutyCycle(n_value)
        print("speed: ", n_value, "val: ", value, "max val: ", max)
    else:
        print("SOMETHING IS WRONG!!!!!!!!!!!! MSG NOT RECVD")
    if (not message == ""):
        print('>',message)
    # message=input(str('Me > '))
    # if message == '[bye]':
    #     mes'Leaving the Chat room'
    #     soc.send(message.encode())
    #     print('\n')

    # break
    # soc.send(message.encode())

