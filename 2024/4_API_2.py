import requests
import json

url = "https://restcountries.com/v3.1/all?fields=name,population,area,subregion,borders"
url2 = "https://restcountries.com/v3.1/name/latvia"
response = requests.get(url)
responseLV = requests.get(url2)
responseParsed = json.loads(response.text)
responseParsedLV = json.loads(responseLV.text)

print(response.json())
valstsSkaits = 0
visaPopulacija = 0
lielakaPopulacija = 0
kopejaPlatiba = 0


for valsts in responseParsed:
    print(valsts['name']['common'])
    valstsSkaits += 1
    visaPopulacija += valsts['population']
    if lielakaPopulacija < valsts['population']:
        lielakaPopulacija = valsts['population']
    kopejaPlatiba += valsts['area']

    print(valsts['population'])



print(valstsSkaits)
videjaPopulacija = visaPopulacija/valstsSkaits
print(videjaPopulacija)
print(lielakaPopulacija)
print(kopejaPlatiba)

for subregion in responseParsedLV:
    print(subregion['subregion'])
    print(subregion['borders'])