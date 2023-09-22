# Eksekverer en python fil.
#execfile("oevelse1.py")

from neopixel import NeoPixel
from machine import Pin

PIXEL_NUMBER = 12 # number of pixels in the Neopixel ring
PIXEL_PIN = 26 # pin atached to Neopixel ring
neopixel = NeoPixel(Pin(PIXEL_PIN, Pin.OUT), PIXEL_NUMBER) # create NeoPixel instance

#neopixel[0] = (255, 255, 255) # set pixel 0 to white (r, g b)

#neopixel[3] = (255, 0, 0) # set pixel 3 to red (r, g b)

#neopixel[6] = (0, 255, 0) # set pixel 6 to green (r, g b)

#neopixel[9] = (0, 0, 255) # set pixel 9 to blue (r, g b)

#neopixel[11] = (0, 255, 255) # set pixel 11 to cyan (r, g b)

#neopixel.write() # write to pixels 

def set_color(red, green, blue):
    for i in range(PIXEL_NUMBER):
        neopixel[i] = (red, green, blue)
    neopixel.write()

set_color(200, 0, 0)

def clear():
    for i in range(PIXEL_NUMBER):
        neopixel[i] = (0, 0, 0)
        neopixel.write()