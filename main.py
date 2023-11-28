from machine import Pin

GREEN_LED = Pin(25, Pin.OUT) # Green

RED_LED = Pin(33, Pin.OUT) # Red

BLUE_LED = Pin(32, Pin.OUT) # Blue

while True:
    RED_LED.on()
    GREEN_LED.on()
    BLUE_LED.on()