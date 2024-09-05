import board
import digitalio as dio
import time

# Setup / initialization
def set_pin_led(pin):
    led = dio.DigitalInOut(pin)
    led.direction = dio.Direction.OUTPUT
    return led
led1 = set_pin_led(board.D2)
led2 = set_pin_led(board.D3)
led3 = set_pin_led(board.D4)
led4 = set_pin_led(board.D5)


def blink(led):
        led.value = not led.value
        time.sleep(0.1)
        led.value = not led.value
        time.sleep(0.1)
        
        
        
while True:
    blink(led1)
    blink(led2)
    blink(led3)
    blink(led4)

