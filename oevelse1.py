import umqtt_robust2 as mqtt
from machine import Pin

# Øvelse 1 Tænd en LED via Adafruit IO

# Her kan i placere globale varibaler, og instanser af klasser

RED_PIN = 26
led1 = Pin(RED_PIN, Pin.OUT)
led1.off()


while True:
    try:
        # Indskriv egen kode her:
        if mqtt.besked == "alive?":
            mqtt.web_print("ESP32 still alive!")
        
        if mqtt.besked == "led_1":
            print("Red LED: ON")
            led1.on()

        if mqtt.besked == "led_0":
            print("Red LED: OFF")
            led1.off()

        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()