from machine import Pin
from time import sleep

led1 = Pin(26, Pin.OUT, value=0)
pb1 = Pin(0, Pin.IN)

while True:
    first = pb1.value()
    sleep(0.01)
    second = pb1.value()
    
    # Tjekker om knap trykkes
    # hvis knap værdi går fra 1 (True) til 0 (False)
    if first == 1 and second == 0:
        print("Knap trykket")
        led1.value(not led1.value())

    # Tjekker om knap slippes
    # hvis knap værdi går fra 0 (False) til (True)
    elif first == 0 and second == 1:
        print("Knap sluppet")