import math
import RPi.GPIO as GPIO
from time import sleep
from client import get_peaks_value


# PINS
MOTOR_PIN = 12

# Base Frequency 
# (optimised motor speed)
BASE_FREQ = 70

# minimum duty to keep ball ready to float
BASE_DUTY = 60

# starting peak value
RESET_PEAK = 16

# global PWM control instance
pi_pwm = None




RESET_INTERVAL = 42


def pwm_init():
    global pi_pwm

    GPIO.setwarnings(False)  # disable warnings
    GPIO.setmode(GPIO.BOARD)  # set pin numbering system
    GPIO.setup(MOTOR_PIN, GPIO.OUT)  # output pin

    pi_pwm = GPIO.PWM(MOTOR_PIN, BASE_FREQ)  # create PWM instance with frequency
    pi_pwm.start(0) # start PWM output


# pwm duty: speed: (60 to 100); x
speed = lambda x, m: round((-40 / m ** 2) * x ** 2 + (80 / m) * x + BASE_DUTY)


def begin():

    counter = 0
    max_peak = RESET_PEAK

    print("begin...")

    while True:

        # increment
        counter += 1

        # keep resetting the max peak value
        if counter % RESET_INTERVAL == 0:
            max_peak = RESET_PEAK

        # received value from the pc
        value = get_peaks_value(); print("peak value: ", value)

        # update max peak
        max_peak = value if max_peak < value else max_peak

        # non-linear map: peaks -> pwm_duty
        n_value = speed(value, max_peak)

        # report
        print("#", counter, "speed: ", n_value, "cur_sp-rate: ", value, "max_rate: ", max_peak)

        # update motor speed
        pi_pwm.ChangeDutyCycle(n_value)

        sleep(0.01)

# test motor pwm speed control
# sine wave
def test_loop():
    speeds = [(round((math.sin(0 + i * ((2 * math.pi) / 100)) + 1) * 50)) for i in range(101)]

    c = 0
    while True:
        c += 1
        speed = speeds[c % len(speeds)]; print('*' * speed)
        pi_pwm.ChangeDutyCycle(speed)
        sleep(0.01)


if __name__ == "__main__":
    test_loop()