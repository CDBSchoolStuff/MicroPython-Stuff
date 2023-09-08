from machine import Pin
from time import sleep

led1 = Pin(26, Pin.OUT, value=0)
pb1 = Pin(4, Pin.IN)

toggle = False

count = 0

while True:
    print("Knap værdi: ", count)
    led1.value(toggle)

    if pb1.value() == False:
        toggle = not toggle
        count = count + 1

    sleep(0.1)
