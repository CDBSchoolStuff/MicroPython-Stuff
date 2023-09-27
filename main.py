from machine import I2C
from eeprom_24xx64 import EEPROM_24xx64

#################################
# Objects and variables
i2c = I2C(0, freq = 400000)

eeprom = EEPROM_24xx64(i2c, 0x50)

#################################
# Program

print("EEPROM 24LC64 via I2C H/W 0 test program,\n")

ssid = ""
password = ""

#eeprom.write_string(1, ssid)
#eeprom.write_string(100, password)

string = eeprom.read_string(1)
string2 = eeprom.read_string(100)
print(string)
print(string2)