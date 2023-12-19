from machine import Pin
from time import sleep

##################################################################
# CONFIGURATION

# Hardware
PIN_OUT = 32
pOut = Pin(PIN_OUT, Pin.OUT)

##################################################################
# OBJECTS


##################################################################
# FUNCTIONS



##################################################################
# PROGRAM

while True:
    pOut.value(1)
    
    sleep(2)
    
    pOut.value(0)
    
    sleep(2)