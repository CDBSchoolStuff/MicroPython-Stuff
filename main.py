from machine import Pin
from time import sleep

##################################################################
# CONFIGURATION

# Hardware
PIN_OUT = 32
pOut = Pin(PIN_OUT, Pin.OUT)

PIN_IN = 34
pIn = Pin(PIN_IN, Pin.IN)

##################################################################
# OBJECTS


##################################################################
# FUNCTIONS



##################################################################
# PROGRAM

while True:
    print("PIn = ", pOut.value())
    
    if pIn.value() == 1:
        pOut.value(1)
    
    else:
        pOut.value(0)

    sleep(1)