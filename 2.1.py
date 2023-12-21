# Øvelse 2.1

# Gennemgå afsnittet “Getting Data Using an API” fra module 4 i bogen.
# Test at i kan få vist vejrdata fra OpenWeatherMap API’en ved brug af
# requests modulet og get metoden.
# https://openweathermap.org/current

API_key = 'aeae29d0ab2a8e2e518db724124a0572'
lat = '55.676098'
lon = '12.568337'

try:
    import urequests as requests
except:
    import requests
    
response = requests.get(
    url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
)

print(response.json())