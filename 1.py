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


import network
from machine import reset

ssid = 'KEA_Starlink'
password = 'KeaStarlink2023'

def do_connect():
    wlan = network.WLAN(network.STA_IF)
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
        
do_connect()