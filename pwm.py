import RPi.GPIO as GPIO
from time import sleep
from client import get_value


# PINS
MOTOR_PIN = 12
MOTOR_FREQ = 70
pi_pwm = None


i = 0
BASE_DUTY = 60
MAX_PEAK = 16
MAX_VAL = 16
RESET_INT = 42


def pwm_init():
    global pi_pwm
    # SETUP
    GPIO.setwarnings(False)  # disable warnings
    GPIO.setmode(GPIO.BOARD)  # set pin numbering system
    GPIO.setup(MOTOR_PIN, GPIO.OUT)  # output pin

    pi_pwm = GPIO.PWM(MOTOR_PIN, MOTOR_FREQ)  # create PWM instance with frequency
    pi_pwm.start(0)


speed = lambda x, m: round((-40 / m ** 2) * x ** 2 + (80 / m) * x + BASE_DUTY)


def begin():
    global i
    max = MAX_PEAK
    print("begin...")
    while True:
        if i % 42 == 0:
            max = MAX_PEAK
        i += 1

        value = get_value()

        print("val: ", value)
        max = value if max < value else max

        n_value = speed(value, max)

        print("#", i, "speed: ", n_value, "cur_rate: ", value, "max_rate: ", max)

        pi_pwm.ChangeDutyCycle(n_value)
        sleep(0.01)
