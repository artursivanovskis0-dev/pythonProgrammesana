import requests
import json
import random

response = requests.get("https://pro2025.azurewebsites.net/books")
dati = response.json()

#4.1
print(F"Statusa kods ir {response.status_code}")
nosaukumi = ""
vecakaGramata = int(dati[0]["year_published"])
kopLppSk = 0
kopCena = 0

for i in dati:
    #4.2
    print(f'Grāmata {i["name"]} ({i["year_published"]}), {i["pages"]} lpp.')
    nosaukumi += i["name"]+ " "
    kopLppSk += int(i["pages"])
    kopCena += int(i["price"])
    if int(i["year_published"]) < vecakaGramata:
        vecakaGramata = int(i["year_published"])
    
#4.3
with open('nosaukumi.json', 'w') as f:
    json.dump(nosaukumi, f)

vidCena = kopCena / len(dati)

#4.4
print(f"Vecākā grāmata ir izdota {vecakaGramata} gadā.")

#4.5
print(kopLppSk)
print(vidCena)

#4.6
def garakais_nosaukums():
    garNosaukums = ""
    indeks = 0
    count = 0
    for i in dati:
        if len(i["name"]) > len(garNosaukums):
            garNosaukums = i["name"]
            indeks = count
        count+=1
    return dati[indeks]

garakaisNosaukums = garakais_nosaukums()

print(f'Garakais nosaukuma autors ir {garakaisNosaukums["author"]} un gads ir {garakaisNosaukums["year_published"]}.')


#4.7
visasGramatas = {}
for i in dati:
    visasGramatas[i["name"]] = i
    if i["author"] == "":
        visasGramatas[i["name"]]["author"] = "Nav norādīts"

print(visasGramatas)

autoriAlfabetaSeciba = set()

autoriUnGramatas = {}

for i in visasGramatas:
    autoriAlfabetaSeciba.add(visasGramatas[i]["author"])
    if visasGramatas[i]["author"] != "":
        if visasGramatas[i]["author"] in autoriUnGramatas:
            autoriUnGramatas[visasGramatas[i]["author"]].append(visasGramatas[i]["name"])
        else:
            autoriUnGramatas[visasGramatas[i]["author"]] = [visasGramatas[i]["name"]]

gramatuSkaits = 0
visvairakGramatuAutors = ""

for autors in autoriUnGramatas:
    if len(autoriUnGramatas[autors]) > gramatuSkaits:
        gramatuSkaits = len(autoriUnGramatas[autors])
        visvairakGramatuAutors = autors

autoriAlfabetaSeciba = list(autoriAlfabetaSeciba)
autoriAlfabetaSeciba = sorted(autoriAlfabetaSeciba)

#4.8
print(autoriAlfabetaSeciba)

#4.9
print(f"Autors, kuram ir visvairāk grāmatu ({gramatuSkaits}), - {visvairakGramatuAutors}:")
for i in autoriUnGramatas[visvairakGramatuAutors]:
    print(i)

#4.10
response2 = requests.get("https://pro2025.azurewebsites.net/journals")
zurnali = response2.json()

randomZurnali = random.sample(zurnali, 10)

zurnalu_saraksts = []

for i in randomZurnali:
    zurnalu_saraksts.append({
        "name": i["name"],
        "publisher": i["publisher"]
    })

print("Sākotnējais žurnālu saraksts:")
for i in zurnalu_saraksts:
    print(f'{i["name"]} – {i["publisher"]}')

def pievienot_zurnalu_sakuma(saraksts):
    nosaukums = input("Ievadi žurnāla nosaukumu: ")
    izdevejs = input("Ievadi žurnāla izdevēju: ")

    jauns_zurnals = {
        "name": nosaukums,
        "publisher": izdevejs
    }

    saraksts.insert(0, jauns_zurnals)

def dzest_pedejo_zurnalu(saraksts):
    saraksts.pop()

pievienot_zurnalu_sakuma(zurnalu_saraksts)
dzest_pedejo_zurnalu(zurnalu_saraksts)

print("Atjauninātais žurnālu saraksts:")
for i in zurnalu_saraksts:
    print(f'{i["name"]} – {i["publisher"]}')