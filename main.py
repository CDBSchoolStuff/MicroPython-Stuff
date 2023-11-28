from machine import Pin, PWM
from time import sleep

##################################################################
# CONFIGURATION

# Hardware
LED_RED_PIN = 33
LED_GREEN_PIN = 25
LED_BLUE_PIN = 32

# Red LED
led_red_freq = 80
led_red_percentage = 50

# Green LED
led_green_freq = 60
led_green_percentage = 0

# Blue LED
led_blue_freq = 60
led_blue_percent = 0


##################################################################
# OBJECTS

LED_RED = PWM(Pin(LED_RED_PIN)) # Red

LED_GREEN = PWM(Pin(LED_GREEN_PIN)) # Green

LED_BLUE = PWM(Pin(LED_BLUE_PIN)) # Blue


##################################################################
# FUNCTIONS

def percentage_to_duty(percent):
    duty_max = 1023 # Duty værdien kan være mellem 0 og 1023
    return int((duty_max / 100) * percent)


##################################################################
# PROGRAM

while True:
    LED_RED.freq(led_red_freq)
    LED_RED.duty(percentage_to_duty(led_red_percentage))
    
    LED_GREEN.freq(led_green_freq)
    LED_GREEN.duty(percentage_to_duty(led_green_percentage))
    
    LED_BLUE.freq(led_blue_freq)
    LED_BLUE.duty(percentage_to_duty(led_blue_percent))
    
    sleep(1)
    