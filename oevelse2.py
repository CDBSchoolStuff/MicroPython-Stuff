import umqtt_robust2 as mqtt
from simpelt_buzzer_program import buzzer

# Her kan i placere globale varibaler, og instanser af klasser

while True:
    try:
        # Indskriv egen kode her:
        if mqtt.besked == "buzz_1":
            buzzer(pwm_buzz, 262, 0.2, 0.2)

        if mqtt.besked == "buzz_2":
            buzzer(pwm_buzz, 0, 0, 0)

        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()