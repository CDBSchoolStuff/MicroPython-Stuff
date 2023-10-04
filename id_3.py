from machine import Pin, ADC
from time import sleep, sleep_ms
from neopixel import NeoPixel
import math

# Initialiserer ADC objekt på pin 34
pot = ADC(Pin(34, Pin.IN), atten=3) # atten 3 = 11db attenuation (150mV - 2450mV)
pot.atten(ADC.ATTN_11DB) # 11db attenuation (150mV - 2450mV)
pot.width(ADC.WIDTH_12BIT) # Bestemmer opløsningen i bits 12 (111111111111 = 4096)

# Instantierer Pin object til at styre led1
# led1 = Pin(26, Pin.OUT, value=0) # Instantierer Pin object til at styre led1

# Instantierer neopixel som objekt
PIXEL_NUMBER = 12 # number of pixels in the Neopixel ring
PIXEL_PIN = 26 # pin atached to Neopixel ring
neopixel = NeoPixel(Pin(PIXEL_PIN, Pin.OUT), PIXEL_NUMBER) # create NeoPixel instance

# Variabel der holder informationer omkring knappen.
pb1 = Pin(4, Pin.IN)
pb2 = Pin(0, Pin.IN)

state = False
pot_val = 0

# Funktion som er ansvarlig for at sætte alle pixels farve på en gang.
# Funktionen modtager 3 argumenter; red, green, blue. Disse henviser til en RGB farvekode.
def set_color_all(red, green, blue):
    for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
        neopixel[number] = (red, green, blue) # Sætter den nuværende pixel i iterationen til den angivede farve.
    neopixel.write() # Skriver værdi til pixel.

def clear():
    set_color_all(0,0,0)

def iterate_pixels(rgb, wait, state_arg):
    for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
        clear()
        neopixel[number] = (rgb) # Sætter den nuværende pixel i iterationen til den angivede farve.
        neopixel.write() # Skriver værdi til pixel.
        sleep_ms(int(wait/100))


while True: # Uendeligt while loop    
    button1 = pb1.value()
    button2 = pb2.value()
    
    # Tjekker om knap trykkes
    # hvis knap værdi går fra 1 (True) til 0 (False)
    if button1 == 0:
        print("Knap1 trykket")
        state = True
        print("State=", state)
    
    if button2 == 0:
        print("Knap2 trykket")
        state = False
        print("State=", state)
    
    if state == True:
        pot_val = pot.read() # Gemmer aflæsningen af ADC objektets read metode i variablen pot_val
        print("Analog potentiometer vaerdi:      ", pot_val) # printer 12Bit ADC værdien

    color = (0,25,0)
    iterate_pixels(color, pot_val, state)

#----------------------------