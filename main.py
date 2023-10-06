import adafruit_gps_main
import _thread
from time import sleep, sleep_ms
from neopixel import NeoPixel
from machine import Pin
import umqtt_robust2 as mqtt

PIXEL_NUMBER = 12 # number of pixels in the Neopixel ring
PIXEL_PIN = 26 # pin atached to Neopixel ring
neopixel = NeoPixel(Pin(PIXEL_PIN, Pin.OUT), PIXEL_NUMBER) # create NeoPixel instance

gps = adafruit_gps_main.gps


def set_color_all(red, green, blue):
    for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
        neopixel[number] = (red, green, blue) # Sætter den nuværende pixel i iterationen til den angivede farve.
    neopixel.write() # Skriver værdi til pixel.

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

# ------------ Øvelse 3.4 ------------

def send_speed():
    speed = adafruit_gps_main.gps.get_speed()
    mqtt.web_print(speed, 'chbo0003/feeds/speedfeed') 
    sleep(4)

# ------------------------------------

# --------- Øvelse 3.2 & 3.3 ---------

def connection_checker():
        if gps.receive_nmea_data() :
            if gps.get_speed() != -999 and gps.get_latitude() != -999.0 and gps.get_longitude() != -999.0 and gps.get_validity() == "A":
                return True
            else:
                return False
        else:
            return False

def gps_checker_thread():
    prev_value = False
    is_connected = False
    while True: 
        is_connected = connection_checker()

        if is_connected and prev_value == False:
            print("GPS forbundet!")
            fade_in_out('green', 0)
            prev_value = True

        if is_connected and prev_value == True:
            send_speed()
            set_color_all(0, 50, 0)

        if is_connected == False:
            print("waiting for GPS data - move GPS to place with access to the sky...")
            fade_in_out('red', 0)
            prev_value = False
        sleep(6)

# ------------------------------------

_thread.start_new_thread(adafruit_gps_main.adafruit_gps_thread, ())
_thread.start_new_thread(gps_checker_thread, ())

# Eksekverer en python fil.
# execfile("adafruit_gps_main.py")