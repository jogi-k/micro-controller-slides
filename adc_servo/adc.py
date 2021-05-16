"""CircuitPython reading a ADC-Value (from poti) """
"""Witten for Raspi - Pico by Jogi"""

import time
import board
import analogio


poti = analogio.AnalogIn(board.GP28)

while True:
    print(poti.value)
    time.sleep(1)

