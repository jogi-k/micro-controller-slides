""" Circuit-Python Example for Raspberry-Pi Pico. Blinks the built-in LED."""
import board
import digitalio
import time
     
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
     
while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
