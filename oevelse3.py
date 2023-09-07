# Følgende fire linjer definerer variabler der bliver tildelt en værdi i enten intiger(hel-tal) eller float(komma-tal)
biler = 100 # Int
plads_i_en_bil = 4.0 # Float
førere = 30
passagerer = 90

# Definerer en variabel som holder på differensen mellem "biler" og "førere" variablerne.
biler_ude_af_drift = biler - førere

# Definerer en variabel der modtager sin værdi fra variablen "førere".
biler_i_kørsel = førere

# Definerer variablen "samlet_bil_kapacitet" som holder på produktet af "biler_i_kørsel" og "plads_i_en_bil" variablerne.
samlet_bil_kapacitet = biler_i_kørsel * plads_i_en_bil

# Definerer variablen "gennemsnit_af_passagerer_per_bil" som holder på kvotienten af "passagerer" og "biler_i_kørsel".
gennemsnit_af_passagerer_per_bil = passagerer / biler_i_kørsel

# Printer text i terminalen baseret på de definerede variabler og strings.
print("Der er", biler, " biler til rådighed.")
print("Der er kun", førere, "førere til rådighed.")
print("Der vil være", biler_ude_af_drift, "tomme biler i dag.")
print("Vi kan transportere", samlet_bil_kapacitet, "personer i dag.")
print("Vi har", passagerer, "passagerer i dag.")
print("Vi skal cirka putte", gennemsnit_af_passagerer_per_bil, "i hver bil.")
print("Vi skal cika putte", gennemsnit_af_passagerer_per_bil, "i hver bil.")

# Øvelse 3.1: Fejlen beskrevet i øvelse 3.1 skyldes at variablen "samlet_bil_kapacitet" mangler at blive defineret.