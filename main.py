#!/home/pi/openday/opendemo/bin/python

from client import get_socket
from pwm import pwm_init, begin

if __name__ == "__main__":
    pwm_init()
    get_socket()
    begin()
