#!/home/pi/openday/opendemo/bin/python

from client import get_socket
from pwm import pwm_init, begin




def main():
     # set up PWM on RPi
    pwm_init()

    # set up Socket connections
    get_socket()

    # start the demo!
    begin()


if __name__ == "__main__":

    main()
