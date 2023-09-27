from neopixel import NeoPixel
from machine import Pin
from time import sleep, sleep_ms

PIXEL_NUMBER = 12 # number of pixels in the Neopixel ring
PIXEL_PIN = 26 # pin atached to Neopixel ring
neopixel = NeoPixel(Pin(PIXEL_PIN, Pin.OUT), PIXEL_NUMBER) # create NeoPixel instance

# ---------- Øvelse 3.1 ----------

# Funktion som er ansvarlig for at sætte enkelte pixels farve. 
# Funktionen modtager 4 argumenter; red, green, blue og pixels. De første tre er til at bestemme farvekoden, og den sidste "pixels" er en liste over pixels som ønskes at blive ændret (Mellem 0 og 11 i dette tilfælde)
# def set_color(red, green, blue, pixels):
#     for number in pixels: # Itererer mellem hvert element i listen "pixels".
#         neopixel[number] = (red, green, blue) # Her sættes RGB værdierne for en pixel. "number" her hentyder til en pixel i listen "pixels".
#     neopixel.write() # Skriver værdi til pixel.

# set_color(0, 50, 0, [0, 1, 2]) # Sætter pixel 1, 2 og 3 til grøn.
# set_color(0, 0, 50, [3, 4, 5]) # Sætter pixel 3, 4 og 5 til blå.
# set_color(50, 0, 0, [6, 7, 8]) # Sætter pixel 6, 7 og 8 til rød.
# set_color(50, 50, 0, [9, 10, 11]) # Sætter pixel 9, 10 og 11 til gul.
# --------------------------------

# ---------- Øvelse 3.2 ----------
# count = 0 # Denne variablen har til ansvar at holde styr på hvor mange gange loopet har kørt.

# Funktion som er ansvarlig for at sætte alle pixels farve på en gang.
# Funktionen modtager 3 argumenter; red, green, blue. Disse henviser til en RGB farvekode.
# def set_color_all(red, green, blue):
#     for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
#         neopixel[number] = (red, green, blue) # Sætter den nuværende pixel i iterationen til den angivede farve.
#     neopixel.write() # Skriver værdi til pixel.

# # Funktion som er til ansvar for at nulstille/slukke alle pixels.
# # Funktionen modtager ingen argumenter.
# def clear():
#     for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
#         neopixel[number] = (0, 0, 0) # Sætter den nuværende pixel i iterationen til at have farvekoden "0,0,0" (Dette slukker for dem).
#         neopixel.write()

# # Løkke som kører så længe at variablen count er mindre end 10.
# while count < 10:
#     count = count + 1 # Inkrementer count med 1
#     set_color_all(50, 0, 0) # Kalder set_color_all() funktionen for at sætte alle pixels til at være røde.
#     sleep(1) # Vent 1 sekund
#     clear() # Kalder på clear() funktionen, som nulstiller alle pixels.
#     sleep(1) # Vent 1 sekund
# --------------------------------

# ---------- Øvelse 3.3 ----------
# pulse_strength = 50

# def fade_in_out(color, wait):
#     for i in range(0, 4 * 256, 8):
#         for number in range(PIXEL_NUMBER):
#             if (i // 256) % 2 == 0:
#                 value = i & 0xff
#             else:
#                 value = 255 - (i & 0xff)
#                 if color == 'red':
#                     neopixel[number] = (value, 0, 0)
#                 elif color == 'green':
#                     neopixel[number] = (0, value, 0)
#                 elif color == 'blue':
#                     neopixel[number] = (0, 0, value)
#                 elif color == 'purple':
#                     neopixel[number] = (value, 0, value)
#                 elif color == 'yellow':
#                     neopixel[number] = (value, value, 0)
#                 elif color == 'teal':
#                     neopixel[number] = (0, value, value)
#                 elif color == 'white':
#                     neopixel[number] = (value, value, value)
#             neopixel.write()
#         sleep_ms(wait)

# fade_in_out('red', 0)
# fade_in_out('green', 10)
# fade_in_out('blue', 25)
# fade_in_out('purple', 10)
# fade_in_out('yellow', 10)
# fade_in_out('teal', 10)
# fade_in_out('white', 10)
# sleep(1)
# --------------------------------

# ---------- Øvelse 3.4 ----------
from machine import PWM

BUZZER_PIN = 12
buzzer = PWM(Pin(BUZZER_PIN, Pin.OUT))
buzzer.duty(0)

# Præcis samme fade funktion som fra tidligere
def fade_in_out(color):
    for i in range(0, 4 * 256, 8):
        for number in range(PIXEL_NUMBER):
            if (i // 256) % 2 == 0:
                value = i & 0xff
            else:
                value = 255 - (i & 0xff)
                if color == 'red':
                    neopixel[number] = (value, 0, 0)
                elif color == 'green':
                    neopixel[number] = (0, value, 0)
                elif color == 'blue':
                    neopixel[number] = (0, 0, value)
                elif color == 'purple':
                    neopixel[number] = (value, 0, value)
                elif color == 'yellow':
                    neopixel[number] = (value, value, 0)
                elif color == 'teal':
                    neopixel[number] = (0, value, value)
                elif color == 'white':
                    neopixel[number] = (value, value, value)
            neopixel.write()

def buzz(frequency, sound_duration, silence_duration, buzz_strength):
    strength = int((512 / 100) * buzz_strength)
    print("Buzz strength: ", strength)
    buzzer.duty(strength)
    buzzer.freq(frequency)
    print("Buzzing!")
    frequency_animation(frequency)
    sleep(sound_duration)
    buzzer.duty(0)
    clear()
    print("Done buzzing...")
    sleep(silence_duration)

'''
Funktion som er ansvarlig for at sætte enkelte pixels farve. 
Funktionen modtager 4 argumenter; red, green, blue og pixels. De første tre er til at bestemme farvekoden, og den sidste "pixels" er en liste over pixels som ønskes at blive ændret (Mellem 0 og 11 i dette tilfælde)
'''
def set_color(red, green, blue, pixels):
    for number in pixels: # Itererer mellem hvert element i listen "pixels".
        neopixel[number] = (red, green, blue) # Her sættes RGB værdierne for en pixel. "number" her hentyder til en pixel i listen "pixels".
    neopixel.write() # Skriver værdi til pixel.

# set_color(0, 50, 0, [0, 1, 2]) # Sætter pixel 1, 2 og 3 til grøn.

# Funktion som er til ansvar for at nulstille/slukke alle pixels.
# Funktionen modtager ingen argumenter.
def clear():
    for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
        neopixel[number] = (0, 0, 0) # Sætter den nuværende pixel i iterationen til at have farvekoden "0,0,0" (Dette slukker for dem).
        neopixel.write()

def frequency_animation(tone_frequency):
    print("Frequency:", tone_frequency)
    if tone_frequency == 200:
        print("Playing Animation 1")
        set_color(50, 0, 0, [1,4,8,11])
    elif tone_frequency == 300:
        print("Playing Animation 2")
        set_color(0, 50, 0, [2,6,10])
    elif tone_frequency == 400:
        print("Playing Animation 3")
        fade_in_out("red")

buzz(200, 1, 0.2, 1)
buzz(300, 1, 0.2, 1)
buzz(400, 1, 1.0, 1)

# --------------------------------

# ---------- Øvelse 3.5 ----------
# Sådan bruges det: 
# Er mqtt.besked lig med "anim_fade", så køres fade animationen.
# Indeholder mqtt.besked strengen "color=", sættes farven til den angivede streng. Eksempel "color=green".


# import umqtt_robust2 as mqtt

# color_string = "white" # Definerer variabel som holder på strengen for dne angivede farve. Som standard er den sat til at være hvid.

# # Præcis samme fade funktion som fra tidligere
# def fade_in_out(color, wait):
#     for i in range(0, 4 * 256, 8):
#         for number in range(PIXEL_NUMBER):
#             if (i // 256) % 2 == 0:
#                 value = i & 0xff
#             else:
#                 value = 255 - (i & 0xff)
#                 if color == 'red':
#                     neopixel[number] = (value, 0, 0)
#                 elif color == 'green':
#                     neopixel[number] = (0, value, 0)
#                 elif color == 'blue':
#                     neopixel[number] = (0, 0, value)
#                 elif color == 'purple':
#                     neopixel[number] = (value, 0, value)
#                 elif color == 'yellow':
#                     neopixel[number] = (value, value, 0)
#                 elif color == 'teal':
#                     neopixel[number] = (0, value, value)
#                 elif color == 'white':
#                     neopixel[number] = (value, value, value)
#             neopixel.write()
#         sleep_ms(wait)

# # Har til ansvar at fjerne kommando delen af beskeden
# def strip_color(color_message):
#     color_message = color_message.strip("color=")
#     return color_message

# while True:
#     try:
#         if mqtt.besked == "anim_fade": # Tjekker om beskeden er lig "anim_fade"
#             print("Running fade animation!")
#             while mqtt.besked == "anim_fade": # "While" loop som sørger for at fade animationen bliver ved med at køre så længe at beskeden er lig "anim_fade".
#                 fade_in_out(color_string, 10) # Kalder på fade_in_out funktionen for at lave fade animationen.
#                 mqtt.sync_with_adafruitIO() # Sikrer at systemet stadig får beskeder fra MQTT selvom vi er inde i et lille while loop.

#         if "color=" in mqtt.besked: # Tjekker om "color=" indgår i beskeden.
#             color_string = strip_color(mqtt.besked) # Bruger funktionen strip_color til at fjerne kommando delen af beskeden, således at kun farve navnet er tilbage i strengen.
#             print("color_string =", color_string)

#         if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
#             mqtt.besked = ""
            
#         mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
#         #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
#         #print(".", end = '') # printer et punktum til shell, uden et enter        
    
#     except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
#         print('Ctrl-C pressed...exiting')
#         mqtt.c.disconnect()
#         mqtt.sys.exit()

# --------------------------------

# ---------- Øvelse 3.5 ----------

# import umqtt_robust2 as mqtt

# def set_color(red, green, blue):
#     for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
#         neopixel[number] = (red, green, blue) # Sætter den nuværende pixel i iterationen til den angivede farve.
#     neopixel.write() # Skriver værdi til pixel.

# '''Denne funktion har til ansvar at omdanne de hexadecimale farvekoder til en rgb tuple'''
# def hex_to_rgb(hex_color):
#     hex_color = hex_color.strip('#') # Fjerner # symbolet fra besked strengen.
#     rgb_list = [] # Definerer en liste til at putte de omdannede værdier ind i.
#     for i in range(0, 6, 2): 
#         rgb_list.append(int(hex_color[i:i + 2], 16)) # ".append" tilføjer et nyt element i listen. Der bruges et "for" loop til at iterere således at der ender med at være tre værdier.
#     return tuple(rgb_list) # Resultatet af funktionen. Her omdannes også listen til en "tuple".

# while True:
#     try:
#         # Tjekker om der er tale om en hexadecimal farvekode ved at kigge efter "#" symbolet og længden på strengen.
#         if "#" in mqtt.besked and len(mqtt.besked) == 7:
#             try:
#                 rgb_tuple = hex_to_rgb(mqtt.besked) # Definerer en tuple variabel som holder på resultatet af hex_to_rgb's omregning af beskeden til RGB værdier
#                 print(f"RGB tuple: {rgb_tuple}") # Printer denne tuple variabel.
#                 set_color(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2], ) # Ændrer værdierne i set_color variablen til dem fra rgb_tuple.
#             except:
#                 print("Wrong hex value!") # Hvis koden under "try" markøren fejler, print en fejl meddelelse i stedet.
        
#         if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
#             mqtt.besked = ""
            
#         mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
#         #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
#         #print(".", end = '') # printer et punktum til shell, uden et enter        
    
#     except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
#         print('Ctrl-C pressed...exiting')
#         mqtt.c.disconnect()
#         mqtt.sys.exit()

# --------------------------------