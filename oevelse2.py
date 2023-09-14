import umqtt_robust2 as mqtt
from machine import Pin
from machine import PWM
from time import sleep

# Her kan i placere globale varibaler, og instanser af klasser
BUZZ_PIN = 26
buzzer = PWM(Pin(BUZZ_PIN, Pin.OUT))
buzzer.duty(0)

print("Kører Øvelse2")


while True:
    try:
        # Indskriv egen kode her:
        if mqtt.besked == "buzz_1":
            print("BUZZING")
            buzzer.duty(512)
            buzzer.freq(500)
            sleep(0.2)
            buzzer.duty(0)
            sleep(0.1)

            buzzer.duty(512)
            buzzer.freq(1300)
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
