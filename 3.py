# Øvelse 3 - JSON

# Lav øvelse 1, 2, 5 og 9 fra linket:
# https://pynative.com/python-json-exercise/

# Husk at bruge ujson hvis øvelser laves på ESP32 med micropython.

# Prøv at print værdien “something interesting here” fra følgende json:
# json_sample = """{"key1":"value1", "key2":[{"key3":"value3"}, {"wow":"something interesting here!"}]"""


try:
    import ujson as json
except:
    import json
    
    
##############################################################
# Exercise 1: Convert the following dictionary into JSON format
data1 = {"key1" : "value1", "key2" : "value2"}

jsonData1 = json.dumps(data1)

print(jsonData1)


##############################################################
# Exercise 2: Access the value of key2 from the following JSON
sampleJson2 = """{"key1": "value1", "key2": "value2"}"""
# write code to print the value of key2

data2 = json.loads(sampleJson2)

print(data2.get("key2"))


##############################################################
# Exercise 5: Access the nested key ‘salary’ from the following JSON
sampleJson5 = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# write code to print the value of salary

data5 = json.loads(sampleJson5)

print(data5["company"]["employee"]["payble"]["salary"])


##############################################################
# Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array
sampleJson9 = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data9 = json.loads(sampleJson9)

print(data9[0].get("name"), data9[1].get("name"))


##############################################################
# Bonus: Prøv at print værdien “something interesting here” fra følgende json:
json_sample = """{"key1":"value1", "key2":[{"key3":"value3"}, {"wow":"something interesting here!"}]"""

dataBonus = json.loads(json_sample)

print(dataBonus.get("key2")[1].get("wow"))