# Importerer påkrævede klasser/biblioteker.
import umqtt_robust2 as mqtt
from machine import Pin
from machine import PWM
from time import sleep

# Definerer variabler sådan så vi kan bruge buzzeren.
BUZZ_PIN = 26
buzzer = PWM(Pin(BUZZ_PIN, Pin.OUT)) # "Pin.OUT" betyder at vi sender et output.
buzzer.duty(0) # Startes med at være slukket (så den ikke hyler)

# Simpel print funktion til at tjekke om programmet bliver eksekveret.
print("Kører Øvelse2")

# Uendeligt loop (Sådan så programmet bliver ved med at køre)
while True:
    
    # "try" bruges her til at nemt kunne bryde loopet ved at gøre det muligt at tilføje en exception(except). (Ikke noget vi har lært om endnu)
    try:
        # Indskriv egen kode her:

        # Hvis beskeden "buzz_1" modtages over MQTT. Spil melodi
        if mqtt.besked == "buzz_1":
            print("BUZZING")
            buzzer.duty(512) # Sætter til 50% styrke. [Duty cycle is between 0 (all off) and 1023 (all on), with 512 being a 50%]
            buzzer.freq(329) # Sætter frekvensen. Når der er tale om en buzzer, ville dette være lyd frekvens.
            sleep(0.2) # Vent 0.2 sekunder
            buzzer.duty(0) # Sætter til 0% styrke.
            sleep(0.1) # Vent 0.1 sekunder

            buzzer.duty(512)
            buzzer.freq(659)
            sleep(0.4)
            buzzer.duty(0)

            buzzer.duty(512)
            buzzer.freq(783)
            sleep(0.4)
            buzzer.duty(0)

            buzzer.duty(512)
            buzzer.freq(739)
            sleep(0.4)
            buzzer.duty(0)

            buzzer.duty(512)
            buzzer.freq(392)
            sleep(0.4)
            buzzer.duty(0)

            buzzer.duty(512)
            buzzer.freq(659)
            sleep(0.4)
            buzzer.duty(0)

            buzzer.duty(512)
            buzzer.freq(783)
            sleep(0.4)
            buzzer.duty(0)

            buzzer.duty(512)
            buzzer.freq(880)
            sleep(0.4)
            buzzer.duty(0)

        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()
