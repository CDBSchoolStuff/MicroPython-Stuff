# Øvelse 2.3

# Prøv at bruge requests modulet og get-metoden til at få data om
# el-spotpriser og print det i shell.
# https://www.energidataservice.dk/tso-electricity/Elspotprices

try:
    import urequests as requests
except:
    import requests
    
response = requests.get(
    url=f'https://api.energidataservice.dk/dataset/Elspotprices?limit=5'
)

print(response.json())