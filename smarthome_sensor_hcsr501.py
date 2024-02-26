# Smart Home PIR sensor program
# MicroPython and ESP32 https://docs.micropython.org/en/latest/esp32/quickref.html
# https://docs.micropython.org/en/latest/library/espnow.html

import network
import espnow

from machine import Pin
import time
from time import ticks_ms, sleep

########################################
# OWN MODULES
from adc_sub import ADC_substitute

########################################
# CONFIGURATION
dashboard_mac_address = b'\xA1\xB2\xC3\xD4\xE5\xF6' # MAC address of dashboard (Educaboard). Byte string format!

# Sensor
sensor_id = "PIR"                      # The sensor ID
pin_sensor = 32                        # The sensor digital GPIO input pin

# Battery
pin_battery = 34                       # The battery measurement input pin, ADC1_6
max_bat_voltage = 4.2
min_bat_voltage = 3.0

########################################
# OBJECTS
# ESP-NOW
sta = network.WLAN(network.STA_IF)     # Or network.AP_IF
sta.active(True)                       # WLAN interface must be active to send()/recv()

en = espnow.ESPNow()                   # ESP-NOW object
en.active(True)                        # Make ESP-NOW active

# Sensor
sensor = Pin(pin_sensor, Pin.IN)
    
# Battery
battery = ADC_substitute(pin_battery)  # The battery object

########################################
# VARIABLES
# Previous values
prev_sensor_value = -999               # The previous value from the sensor
bat_pct = None
prev_bat_pct = -1                      # The previous battery percentage value
buffer = []                            # Opret en tom buffer


# Resistors
resistor1 = 4.70
resistor2 = 4.70
max_spaendingsdeler_voltage_measurement = 2.07   # Ikke brugt, bare til egen info. Målt ved 4.2V input med 2x 4.7k modstande.

########################################
# FUNCTIONS

# Beregner den teoretiske maksimale spænding for spændingsdeleren.
def calc_spaendingsdeler(U, R1, R2):
    U_out = (U * R2) / (R1 + R2)
    return U_out

max_spaendingsdeler_voltage = calc_spaendingsdeler(max_bat_voltage, resistor1, resistor2)
min_spaendingsdeler_voltage = calc_spaendingsdeler(min_bat_voltage, resistor1, resistor2)

print(f"Spaendingsdeler Max Voltage: {max_spaendingsdeler_voltage}")
print(f"Spaendingsdeler Min Voltage: {min_spaendingsdeler_voltage}")

def get_battery_percentage():          # The battery voltage percentage
    
    # Beregn procentdelen af batteriets opladning
    percentage = ((battery.read_voltage() - min_spaendingsdeler_voltage) / (max_spaendingsdeler_voltage - min_spaendingsdeler_voltage)) * 100
    
    # Sørg for, at procentdelen er inden for intervallet 0% til 100%
    percentage = max(0, min(100, percentage))

    return percentage                          # Replace with own math. Use function in adc_sub.py
                                       # Make the result an integer value, and avoid neg. and above 100% values

def calculate_average_battery(window_size, bat_percentage):
    buffer.append(bat_percentage)

    if len(buffer) > window_size:
        buffer.pop(0)  # Fjern ældste værdi, hvis bufferen er fyldt

    if not buffer:
        return 0  # Returner 0, hvis bufferen er tom
    return int(sum(buffer) / len(buffer))

########################################
# PROGRAM

battery_status_start = ticks_ms()
battery_status_period_ms = 1000 # 1000ms = 1s

# INITIALIZATION
# ESP-NOW
en.add_peer(dashboard_mac_address)     # Must add_peer() before send()
en.send(dashboard_mac_address, sensor_id + " ready", False)

print(sensor_id + " ready")

# MAIN (super loop)
while True:
    # Measure the battery percentage.
    # Using ticks_ms to prevent battery changes from spamming too many messages.
    if ticks_ms() - battery_status_start > battery_status_period_ms:
        battery_status_start = ticks_ms()
        
        bat_pct = calculate_average_battery(20, get_battery_percentage())
    
    # Check the sensor
    sensor_value = sensor.value()

    # Send data if there is a change (this principle saves power)
    if bat_pct != prev_bat_pct or sensor_value != prev_sensor_value:
        data_string = sensor_id + '|' + str(time.ticks_ms()) + '|' + str(bat_pct) + '|' + str(sensor_value) # The data to send. CHANGE IT! (Added the "sensor_id")
        
        print("Sending: " + data_string)
        try:
            en.send(dashboard_mac_address, data_string, False)
        except ValueError as e:
            print("Error sending the message: " + str(e))  
        
        # Update the previous values for use next time
        prev_bat_pct = bat_pct
        prev_sensor_value = sensor_value

