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


#--------- Øvelse 2 | Del 2 ---------
# Lav en funktion der kører et for loop som tænder én pixel hele
# vejen rundt i neopixel ringen imens de andre er slukket. Den skal tage 1
# parameter som skal være tiden der skal gå mellem hver pixel der tændes i
# ringen. Tiden skal styres ved at dreje på potentiometeret. 


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
    iterate_pixels(color, pot_val)

#----------------------------