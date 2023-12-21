# Øvelse 5 - Brug af bærerygtigt energi

# Lav program der henter data fra API hvert kvarter og tænder et relæ hvis
# Co2 udledningen kommer under 50g. Per KWh.

# Når relæet har været tændt i 60 minutter skal det slukkes igen. Dette kan
# gøres ved brug af hardware Timers.

# Relæet må kun tændes 1 gang i døgnet og data skal være fra budzoner dk
# 2 på elnettet, dette kan tjekke med localtime eller RTC.datetime.

# (Test det med kortere tids-intevaller først og træk evt. Flere records ud fra
# API og test med værdier der er under tærsklen eller sæt tærsklen under den
# værdi der kommer)

# https://www.energidataservice.dk/tso-electricity/CO2Emis