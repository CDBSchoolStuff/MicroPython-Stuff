from machine import I2C
from machine import Pin
from time import sleep
from mpu6050 import MPU6050
import sys
from neopixel import NeoPixel
import umqtt_robust2 as mqtt

#Initialisering af I2C objekt
i2c = I2C(0)

#Initialisering af mpu6050 objekt
imu = MPU6050(i2c)

PIXEL_NUMBER = 12 # number of pixels in the Neopixel ring
PIXEL_PIN = 26 # pin atached to Neopixel ring
neopixel = NeoPixel(Pin(PIXEL_PIN, Pin.OUT), PIXEL_NUMBER) # create NeoPixel instance

# Diverse variabler:
standing_threshold = 10000 # Ansvarlig for stejlheden af hvornår enheden betegnes som værende stående eller liggende.
number_of_falls = 0
prev_standing = False

def set_color(red, green, blue):
    for number in range(PIXEL_NUMBER): # Itererer mellem alle pixels.
        neopixel[number] = (red, green, blue) # Sætter den nuværende pixel i iterationen til den angivede farve.
    neopixel.write() # Skriver værdi til pixel.

while True:
    try:
        # printer hele dictionary som returneres fra get_values metoden
        imu_data = imu.get_values()
        print(imu_data)

        if (imu_data.get("acceleration x") > standing_threshold or imu_data.get("acceleration x") < -standing_threshold) or (imu_data.get("acceleration y") > standing_threshold or imu_data.get("acceleration y") < -standing_threshold):
            print("Enheden står op!")
            set_color(0,50,0)
            prev_standing = True
        else:
                print("Enheden ligger ned!")
                set_color(50,0,0)
                
                # --------- Del 3 ---------
                if prev_standing == True: # Sørger for at antallet af fald kun inkrementeres hvis der gåes fra stående til liggende tilstand.
                    number_of_falls = number_of_falls + 1
                    print("Antal fald:", number_of_falls)
                    prev_standing = False
                    # --------- Del 6 ---------
                    mqtt.web_print(number_of_falls, 'chbo0003/feeds/ESP32feed')
                    # -------------------------
                # -------------------------
        sleep(1)
    except KeyboardInterrupt:
        print("Ctrl+C pressed - exiting program.")
        sys.exit()