from machine import Pin, ADC
from time import sleep, sleep_ms
from neopixel import NeoPixel
import umqtt_robust2 as mqtt

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

# -------------- Krav --------------
# Løsningen skal kunne styre lysintensiteten på 12 RGB LED’er gennem internettet fra en fjern lokation.	Prioritet: 1



# Funktion som er ansvarlig for at sætte alle pixels farve på en gang.
# Funktionen modtager 3 argumenter; red, green, blue. Disse henviser til en RGB farvekode.
def set_color_all(red, green, blue):
    for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
        neopixel[number] = (red, green, blue) # Sætter den nuværende pixel i iterationen til den angivede farve.
    neopixel.write() # Skriver værdi til pixel.

# Har til ansvar at fjerne kommando delen af beskeden
def strip_lys_styrke(lys_styrke_message):
    lys_styrke_message = lys_styrke_message.strip("lys_styrke=")
    return float(lys_styrke_message)


while True:
    try:
        # Egen kode:
        if "lys_styrke=" in mqtt.besked:
            lys_styrke = strip_lys_styrke(mqtt.besked)
            set_color_all(0, 0, int(255 * lys_styrke))
            print("Lystyrke =", lys_styrke)
            sleep(0.5)
            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')

#----------------------------