import network
from machine import Pin, PWM, reset
from gpio_lcd import GpioLcd


# Øvelse 1

# Lav en boot.py fil der forbinder til starlink wifi og tjek at der forbindes korrekt.
# Gem denne fil på ESP32 som boot.py så der altid forbindes til wifi når den
# bootes op.

# Når der skal forbindes skal det gøres med en funktion og denne funktion skal
# returnere et WLAN objekt. I boot.py skal funktionen kaldes og returværdien
# skal lægges i en variabel kaldet wlan.

# Hvis ikke at der er forbundet inden for 10 sekunder, skal programmet
# fortsætte til main.py filen. Main filen skal angive wifi status kode på LCD
# display og om der er forbundet eller ej.

# Hvis ikke der kan forbindes til starlink så forbind til eget mobile hotspot fra
# laptop.

#########################################################################
# LCD CONFIGURATION

pin_lcd_contrast = 23
contrast_level = 250                        # Varies from LCD to LCD and wanted contrast level: 0-1023
lcd_contrast = PWM(Pin(pin_lcd_contrast))   # Create PWM object from a pin
lcd_contrast.freq(440)                      # Set PWM frequency
lcd_contrast.duty(contrast_level)


#########################################################################
# WIFI CONFIGURATION

ssid = 'KEA_Starlink'
password = 'KeaStarlink2023'

wlan = network.WLAN(network.STA_IF)


#########################################################################
# FUNCTIONS

def do_connect():
    print('WLAN status:', wlan.status())
    wlan.active(True)
    try:
        if not wlan.isconnected():
            print('connecting to network...')
            wlan.connect(ssid, password)
            print('WLAN status:', wlan.status())
            while not wlan.isconnected():
                pass
    except Exception as e:
        print(f"Wifi error '{e}' occured, rebooting system")
        reset()
    finally:
        print(f"Wifi connected to '{ssid}'!")
        print('WLAN status:', wlan.status())


def Print_LCD():
    # Create the LCD object
    lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                  d4_pin=Pin(33), d5_pin=Pin(32), d6_pin=Pin(21), d7_pin=Pin(22),
                  num_lines=4, num_columns=20)
    lcd.clear()
    lcd.putstr("Programmering 11:")
    lcd.move_to(0, 1)
    lcd.putstr("Wifi og API")    
    lcd.move_to(0, 2)
    lcd.putstr("------------------")
    lcd.move_to(0, 3)
    lcd.putstr(f"WLAN status: {wlan.status()}")


#########################################################################
# FUNCTIONS TO RUN ON BOOT

do_connect()
Print_LCD()


