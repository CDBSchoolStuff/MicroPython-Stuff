# Python dictionary {} der indeholder login oplysninger
# Undlad at uploade denne fil til github når den er udfyldt

# ADAFRUIT_IO_URL behøves ikke at ændres

# ADAFRUIT_IO_FEEDNAME behøves ikke at ændres (men skal oprettes med samme navn)
# men der skal oprettes en feed med samme navn på adafruit.io

from machine import I2C
from eeprom_24xx64 import EEPROM_24xx64

i2c = I2C(0, freq = 400000)

eeprom = EEPROM_24xx64(i2c, 0x50)

credentials = {
    #'ssid' : 'KEA_Starlink',
    #'password' : 'KeaStarlink2023',
    
    ssid_string = eeprom.read_string(1)
    password_string = eeprom.read_string(100)

    'ssid' : '%s' % ssid_string,
    'password' : '%p' % password_string,
    'ADAFRUIT_IO_URL' : b'io.adafruit.com',
    'ADAFRUIT_USERNAME' : b'DIT ADAFRUIT BRUGERNAVN',
    'ADAFRUIT_IO_KEY' : b'DIN ADAFRUIT IO KEY',
    'ADAFRUIT_IO_FEEDNAME' : b'ESP32feed'
    }