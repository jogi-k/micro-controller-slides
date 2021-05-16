"""CircuitPython Essentials Servo standard servo example"""
"""Adapted to Raspi - Pico and extended for reading poti by Jogi"""

import time
import board
import pwmio
import analogio
import digitalio
from adafruit_motor import servo


# equivalent of map-function in Arduino-C++ 
def _map(x, in_min, in_max, out_min, out_max):
	return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


# create a PWMOut object on Pin GP15.
pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo, with the help of the above defined PWM
my_servo = servo.Servo(pwm)

# This is just to have a second +3.3 V as I need two but only have one available. Thats for the poti, so no
# real current is drawn ...

out = digitalio.DigitalInOut(board.GP27)
out.direction = digitalio.Direction.OUTPUT
out.value = True


poti = analogio.AnalogIn(board.GP28)

while True:
    print(poti.value)
    time.sleep(0.1)
    angle = _map(poti.value, 0, 65535, 0, 180 )
    my_servo.angle = angle
    

