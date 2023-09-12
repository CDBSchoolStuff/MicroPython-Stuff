from machine import Pin
from time import sleep

# Definerer en variabel der holder information omring den røde LED. Såsom at den sidder på pin 26 og er en Pin.OUT type.
# (Den røde LED er aktiv lav)
RED_LED = Pin(26, Pin.OUT)
RED_LED.off()

# Den gule LED har omvendt spænding og skal derfor starte med at sættes til "off" for at tænde.
YELLOW_LED = Pin(12, Pin.OUT)
YELLOW_LED.on()

GREEN_LED = Pin(13, Pin.OUT)
GREEN_LED.off()

# Variablen der holder styr på hvor mange gange loopet har kørt.
count = 0

while True:
  # Slukker alle LED'erne.
  RED_LED.off()
  YELLOW_LED.on()
  GREEN_LED.off()

  # Når variablen "count" er lig 1.
  if count == 1:
    # Tænd RED_LED. (Sæt den til modsatte værdi)
    RED_LED.value(not RED_LED.value())

  # Når variablen "count" er lig 2.
  elif count == 2:
    # Tænd YELLOW_LED. (Sæt den til modsatte værdi)
    YELLOW_LED.value(not YELLOW_LED.value())
  
   # Når variablen "count" er lig 3.
  elif count == 3:
    # Tænd GREEN_LED. (Sæt den til modsatte værdi)
    GREEN_LED.value(not GREEN_LED.value())

  # Gælder ingen af ovenstående statements. Nulstilles "count" variablen.
  else:
    count = 0

  # Tæl "count" variablen op med 1. (Kører ved hvert loop)
  count = count + 1
  
  # Vent 1 sekund med at fortsætte.
  sleep(1.0)