from machine import Pin, ADC
from time import sleep, sleep_ms
from neopixel import NeoPixel
import math


# Instantierer Pin object til at styre led1
# led1 = Pin(26, Pin.OUT, value=0) # Instantierer Pin object til at styre led1

# Instantierer neopixel som objekt
PIXEL_NUMBER = 12 # number of pixels in the Neopixel ring
PIXEL_PIN = 26 # pin atached to Neopixel ring
neopixel = NeoPixel(Pin(PIXEL_PIN, Pin.OUT), PIXEL_NUMBER) # create NeoPixel instance


# Variabel der holder informationer omkring knappen.
pb1 = Pin(4, Pin.IN)

def clear():
    set_color_all(0,0,0)
        
count = 0

while True: # Uendeligt while loop
    first = pb1.value()
    sleep(0.01)
    second = pb1.value()
    
    # Tjekker om knap trykkes
    # hvis knap værdi går fra 1 (True) til 0 (False)
    if first == 1 and second == 0:
        neopixel[count] = (0,0,0)
        count = count + 1
        print("Knap trykket")
        neopixel[count] = (50,0,0)
        neopixel.write()
        if count >= 11:
            count = 0


    # Tjekker om knap slippes
    # hvis knap værdi går fra 0 (False) til (True)
    elif first == 0 and second == 1:
        print("Knap sluppet")