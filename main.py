from neopixel import NeoPixel
from machine import Pin
import umqtt_robust2 as mqtt
from time import sleep, sleep_ms

PIXEL_NUMBER = 12 # number of pixels in the Neopixel ring
PIXEL_PIN = 26 # pin atached to Neopixel ring
neopixel = NeoPixel(Pin(PIXEL_PIN, Pin.OUT), PIXEL_NUMBER) # create NeoPixel instance

BUZZER_PIN = 25
buzzer = Pin(BUZZER_PIN, Pin.OUT)
buzzer.off()

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
count = 0 # Denne variablen har til ansvar at holde styr på hvor mange gange loopet har kørt.

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
pulse_strength = 50

def fade_in_out(color, wait):
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
        sleep_ms(wait)

fade_in_out('red', 0)
fade_in_out('green', 10)
fade_in_out('blue', 25)
fade_in_out('purple', 10)
fade_in_out('yellow', 10)
fade_in_out('teal', 10)
fade_in_out('white', 10)
sleep(1)
# --------------------------------

# ---------- Øvelse 3.4 ----------





# def hex_to_rgb(hex_color):
#     hex_color = hex_color.strip('#')
#     rgb_list = []
#     for index in range(0, 6, 2)
#         rgb.list.append(int(hex_color[index:index + 2], 16))
#     return tuple(rgb_list)

# while True:
#     try:
#         if "#" in mqtt.besked and len(mqtt.besked) == 7:
#             try:
#                 rgb_tuple = hex_to_rgb(mqtt.besked)
#                 print(f"RGB tuple: {rgb_tuple}")
#                 set_color(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
#             except:
#                 print("Wrong hex value!")

# --------------------------------