import board
import time
from digitalio import DigitalInOut, Direction

led = DigitalInOut(board.D2)
led.direction = Direction.OUTPUT
led.value = True

while True:
    led.value = not led.value
    time.sleep(0.1)
