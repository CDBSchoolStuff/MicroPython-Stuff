# Importerer påkrævede klasser/biblioteker.
import umqtt_robust2 as mqtt
from machine import Pin
from time import sleep

# Simpel print funktion til at tjekke om programmet bliver eksekveret.
print("Kører Oevelse3")

# Definerer variabler sådan så vi kan bruge pb1 knappen.
BUTTON_PIN = 4
pb1 = Pin(BUTTON_PIN, Pin.IN) # "Pin.IN" betyder at vi forventer at modtage noget input.

# Definerer variablen "toggle", som har til ansvar at fungere som on/off switch, men uden at være en boolean (MQTT ville ikke samarbejde hvis vi lavede den som en bool)
toggle = 0

# Uendeligt loop (Sådan så programmet bliver ved med at køre)
while True:
    try:
        # Indskriv egen kode her:

        # Definerer to variabler "first" og "second" med en sleep funktion imellem. Disse kan så bruges i et "if" statement, hvor at de kan sammenlignes og derved finde ud af om knappen bliver trykket uden prel.
        first = pb1.value()
        sleep(0.01)
        second = pb1.value()
        
        # Hvis begge udtryk er sande.
        if first == 1 and second == 0:            
            print("Knap trykket") # Printer til terminalen.
            
            # Hvis toggle er lig "0".
            if toggle == 0:
                toggle = toggle + 1 # Plus toggle variablen med "1".
            
            # Hvis toggle er lig "1".
            elif toggle == 1:
                toggle = toggle - 1 # Minus toggle variablen med "1".
                
            # Send værdien af variablen "toggle" til MQTT.
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