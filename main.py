from machine import I2C
from time import sleep_ms
# from device_scanner import i2c_scanner # Hjemmelavet bibliotek


# Configuration
eeprom_i2c_addr = 0x50
eeprom_mem_address = 32


# Objects and variables
i2c = I2C(0)


def write_byte(i2cAddr, addr, val):
    ba = bytearray(1)
    ba[0] = val

    res = i2c.writeto_mem(i2cAddr, addr, ba, addrsize = 16)
    sleep_ms(5) # Needed due to EEPROM write timing

    return res

def read_byte(i2cAddr, addr):
    val = i2c.readfrom_mem(i2cAddr, addr, 1, addrsize = 16)
    return val[0]

print("EEPROM test program\n")

write_byte(eeprom_i2c_addr, eeprom_mem_address, 80)

value = read_byte(eeprom_i2c_addr, eeprom_mem_address)
print(value)
print("%d: %02d/0x%02x" % (eeprom_mem_address, value, value))


# Kører i2c scanner funktionen
#--------------------------------------

# while True:
#     i2c_scanner(i2c)

#--------------------------------------


