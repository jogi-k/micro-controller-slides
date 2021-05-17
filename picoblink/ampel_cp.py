""" Circuit-Python Example for Raspberry-Pi Pico. Blinks the built-in LED."""
import board
import digitalio
import time
     
red = digitalio.DigitalInOut(board.GP10)
red.direction = digitalio.Direction.OUTPUT
yellow = digitalio.DigitalInOut(board.GP11)
yellow.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.GP12)
green.direction = digitalio.Direction.OUTPUT
     
red.value = False     
yellow.value = False     
green.value = False     
     
while True:
    red.value = True
    time.sleep(2)
    yellow.value = True
    time.sleep(1)
    red.value = False     
    yellow.value = False     
    green.value = True
    time.sleep(3)
    yellow.value = True     
    green.value = False
    time.sleep(1)
    yellow.value = False     
    
