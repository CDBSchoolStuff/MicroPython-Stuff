from machine import I2C
from time import sleep, sleep_ms, ticks_ms
from ina219_lib import INA219

##################################################################
# CONFIGURATION
i2c = I2C(0, freq = 400000)
ina = INA219(i2c, 0x40)

start_time = ticks_ms()
test_time_ms = 1000
seperation_symbol = ";"

data_list = []


##################################################################
# FUNCTIONS



##################################################################
# PROGRAM

while True:
    time = ticks_ms() - start_time
    if time < test_time_ms:
        current = ina.get_current()
        
        #print(time)
        #print(current)
        
        data_string = str(time) + seperation_symbol + str(current)
        
        data_list.append(data_string)
    
    else:
        print("Test is over,", time, "ms has passed.")
        #print(current_list)

        with open('data.txt', 'w+') as df:
            df.write('tid' +  seperation_symbol + 'strøm\n')
            for line in data_list:
                df.write(f"{line}\n")

        break