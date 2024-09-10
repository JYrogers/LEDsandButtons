
import board
import digitalio as dio
import time

led = dio.DigitalInOut(board.D4)
led.direction = dio.Direction.OUTPUT
led.value = True

led2 = dio.DigitalInOut(board.D5)
led2.direction = dio.Direction.OUTPUT
led2.value = True 


button = dio.DigitalInOut(board.D2)
button.direction = dio.Direction.INPUT

button2 = dio.DigitalInOut(board.D3) 
button2.direction = dio.Direction.INPUT

led_status = False

btn2 = False

while True:    
    if not button.value:
        led_status = not led_status
        time.sleep(0.2)
            
    if led_status:
        led_status = False
        led.value = not led.value
        led2.value = not led.value
        time.sleep(.2)  
             
    if not button2.value:
        btn2 = not btn2
        time.sleep(.20)
         
    if btn2:
        btn2 = False
        led.value = not led.value
        led2.value = led.value
            
