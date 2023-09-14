import umqtt_robust2 as mqtt
from machine import Pin
from time import sleep

print("Kører Oevelse3")

BUTTON_PIN = 4
pb1 = Pin(BUTTON_PIN, Pin.IN)


toggle = 0

while True:
    try:
        # Indskriv egen kode her:
        first = pb1.value()
        sleep(0.01)
        second = pb1.value()
        
        if first == 1 and second == 0:            
            print("Knap trykket")
            
            if toggle == 0:
                toggle = toggle + 1
            
            elif toggle == 1:
                toggle = toggle - 1
                
            mqtt.web_print(toggle)

        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()