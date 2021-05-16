"""CircuitPython Essentials Servo standard servo example"""
"""Adapted to Raspi - Pico by Jogi"""

import time
import board
import pwmio
from adafruit_motor import servo
     
# create a PWMOut object on Pin GP15.
pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)
     
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
     
while True:
    for angle in range(0, 180, 10):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -20): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
