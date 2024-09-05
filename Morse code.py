import board
import digitalio as dio
import time

# Setup / initialization
led = dio.DigitalInOut(board.D2)
led.direction = dio.Direction.OUTPUT


def dot():
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

def dash():
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(0.5)

def tween():
    led.value = False
    time.sleep(0.5)

def separator():
    led.value = False
    time.sleep(1.5)

def letterR():
    dot()
    tween()
    dash()

def letterO():
    dash()
    dash()
    dash()

def letterG():
    dash()
    dash()
    dot()

def letterE():
    dot()

def letterS():
    dot()
    dot()
    dot()

letterR()
separator()
letterO()
separator()
letterG()
separator()
letterE()
separator()
letterR()
separator()
letterS()
