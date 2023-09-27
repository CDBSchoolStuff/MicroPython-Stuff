from machine import I2C, Pin, SoftI2C
from time import sleep

i2c = I2C(0)

print("Running I2C scanner\n")

def i2c_scanner(i2c_arg):
    # Scan for connected devices
    devices_identified = i2c_arg.scan()

    #print the result
    devices_count = len(devices_identified)
    print("Total number of devides: %d" % devices_count)

    if devices_count == 112:
        print("Looks like the I2C bus pull-up resistors are missing")
    else:
        for i in range(devices_count):
            print("Device found at address: 0x%02X" % devices_identified[i])
    print()
    sleep(1)