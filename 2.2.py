# Øvelse 2.2

# Prøv at bruge requests modulet og get-metoden til at få data om CO2
# og print det i shell.
# https://www.energidataservice.dk/tso-electricity/CO2Emis

try:
    import urequests as requests
except:
    import requests
    
response = requests.get(
    url=f'https://api.energidataservice.dk/dataset/CO2Emis?limit=5'
)

print(response.json())