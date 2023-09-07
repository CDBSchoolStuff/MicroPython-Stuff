from machine import Pin
from time import sleep

# Definerer en variabel der holder information omring den røde LED. Såsom at den sidder på pin 26 og er en Pin.OUT type.
# (Den røde LED er aktiv lav)
RED_LED = Pin(26, Pin.OUT)
RED_LED.on()

# Den gule LED har omvendt spænding og skal derfor starte med at sættes til "off" for at tænde.
YELLOW_LED = Pin(12, Pin.OUT)
YELLOW_LED.off()

GREEN_LED = Pin(13, Pin.OUT)
GREEN_LED.on()

while True:
  # Sætter værdien af "RED_LED" til den modsatte værdi. (Er LED'en tændt, så vil den slukke og omvendt)
  RED_LED.value(not RED_LED.value())
  YELLOW_LED.value(not YELLOW_LED.value())
  GREEN_LED.value(not GREEN_LED.value())

  if RED_LED.value():
    print("Red LED is ON")
  else:
    print("Red LED is OFF")
  
  sleep(1.0)