from machine import Pin, ADC
from time import sleep_ms

# Initialiserer ADC objekt på pin 34
pot = ADC(Pin(34, Pin.IN), atten=3) # atten 3 = 11db attenuation (150mV - 2450mV)
pot.atten(ADC.ATTN_11DB) # 11db attenuation (150mV - 2450mV)
pot.width(ADC.WIDTH_12BIT) # Bestemmer opløsningen i bits 12 (111111111111 = 4096)
led1 = Pin(26, Pin.OUT, value=0) # Instantierer Pin object til at styre led1

while True: # Uendeligt while loop
    pot_val = pot.read() # Gemmer aflæsningen af ADC objektets read metode i variablen pot_val
    spaending = pot_val * (3.3 / 4096) # Udregner spændingen og gemmer i variabel
    print("Analog potentiometer vaerdi:      ", pot_val) # printer 12Bit ADC værdien
    print("\nAnalog potentiometer spaending: ", spaending) # Printer spændingen på GPIO 34
    led1.value(not led1.value()) # blinker LED
    # kalder sleep_ms funktionen og giver pot_val variablen som argument
    # (for at justere tiden med potmeter)
    sleep_ms(1 + pot_val)