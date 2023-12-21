# Øvelse 4

# Brug eksemplet fra øvelse 1 så der forbindes til wifi når systemet bootes op.

# Hent tiden når systemet bootes op og brug ntptime.settime() til at instille
# korrekt dansk tid. Se https://bhave.sh/micropython-ntp/

# Vis korrekt dato og tid på LCD display

# Test at det virker ved at reboote ESP32 uden at thonny er åbent.

# Hvis der er Wifi så sørg for at RTC også instilles med korrekt tid.
# Og sørg for at tiden på display vises med tiden fra RTC.

# Bonus opgave:
# Hvis ikke der forbindes til wifi, skal den tage tiden fra GPS modulet. Og ellers
# stille tiden efter sidste gang der var wifi (som skal gemmes der).