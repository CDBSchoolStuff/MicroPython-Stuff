from machine import Pin, I2C
from time import sleep, sleep_ms, ticks_ms
from ina219_lib import INA219

##################################################################
# CONFIGURATION
i2c = I2C(0, freq = 400000)
ina = INA219(i2c, 0x40)

start_time = ticks_ms()
test_time_ms = 1000


##################################################################
# FUNCTIONS



##################################################################
# PROGRAM

while True:
    time = ticks_ms() - start_time
    if time < test_time_ms:
        current = ina.get_current()
        #print(current)
        print(time)
    else:
        print("Test is over,", time, "ms has passed.")
        break