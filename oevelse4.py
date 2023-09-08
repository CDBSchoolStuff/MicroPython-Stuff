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

count = 0

while True:
  RED_LED.off()
  YELLOW_LED.on()
  GREEN_LED.off()

  if count == 1:
    RED_LED.value(not RED_LED.value())

  elif count == 2:
    YELLOW_LED.value(not YELLOW_LED.value())
  
  elif count == 3:
    GREEN_LED.value(not GREEN_LED.value())

  else:
    count = 0

  count = count + 1
  
  sleep(1.0)