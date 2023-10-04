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

state = False

# Funktion som er ansvarlig for at sætte alle pixels farve på en gang.
# Funktionen modtager 3 argumenter; red, green, blue. Disse henviser til en RGB farvekode.
def set_color_all(red, green, blue):
    for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
        neopixel[number] = (red, green, blue) # Sætter den nuværende pixel i iterationen til den angivede farve.
    neopixel.write() # Skriver værdi til pixel.

def clear():
    set_color_all(0,0,0)

def iterate_pixels(rgb, wait):
    for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
        clear()
        neopixel[number] = (rgb) # Sætter den nuværende pixel i iterationen til den angivede farve.
        neopixel.write() # Skriver værdi til pixel.
        sleep_ms(int(wait/100))

while True: # Uendeligt while loop
    pot_val = pot.read() # Gemmer aflæsningen af ADC objektets read metode i variablen pot_val
    spaending = pot_val * (3.3 / 4096) # Udregner spændingen og gemmer i variabel
    print("Analog potentiometer vaerdi:      ", pot_val) # printer 12Bit ADC værdien
    # print("\nAnalog potentiometer spaending: ", spaending) # Printer spændingen på GPIO 34
    color = (0,25,0)


    first = pb1.value()
    sleep(0.01)
    second = pb1.value()
    
    # Tjekker om knap trykkes
    # hvis knap værdi går fra 1 (True) til 0 (False)
    if first == 1 and second == 0:
        print("Knap trykket")
        if state == False:
            state = True
        elif state == True:
            state = False

    # Tjekker om knap slippes
    # hvis knap værdi går fra 0 (False) til (True)
    elif first == 0 and second == 1:
        print("Knap sluppet")

    if state == True:
        iterate_pixels(color, pot_val)
    
    print("State=", state)

#----------------------------