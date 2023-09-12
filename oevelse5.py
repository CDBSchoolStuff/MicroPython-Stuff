from machine import Pin
from time import sleep

led1 = Pin(26, Pin.OUT, value=0)

# Variabel der holder informationer omkring knappen.
pb1 = Pin(4, Pin.IN)

# Boolean variabel der bruges som toggler hver gang knappen trykkes.
toggle = False

count = 0

while True:
    # Printer antallet knappen er blevet trykket.
    print("Knap værdi: ", count)
    
    # Sætter led1 til hvad end "toggle" værdien er.
    led1.value(toggle)

    # Hvis knappens værdi er lig "False".
    if pb1.value() == False:
        # Hvad end "toggle" variablen er lige nu, sæt den til det modsatte.
        toggle = not toggle
        # Tæller op med 1 for hver gang at knappen trykkes (Uden debounce fix)
        count = count + 1

    sleep(0.1)
