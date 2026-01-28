import requests
import json
import sqlite3
import os

# if os.path.exists("valsts.db"):
#     os.remove("valsts.db")
# else:
#     print("fails neeksiste")
con = sqlite3.connect("valsts.db")

response = requests.get(f"https://restcountries.com/v3.1/all?fields=name,population")
dati = response.json()

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Valsts(ValstsID INTEGER UNIQUE PRIMARY KEY, Nosaukums VARCHAR, OficialaisNosaukums VARCHAR, Populacija INTEGER)")



country = input("Ievadi valsti: ")

cur.execute(f"""SELECT * from Valsts where Nosaukums="{country}" """)
res = cur.fetchall()
print(len(res))
if (len(res) >0):
    print("Mums jau ir informācija par valsti")
else:
    print("Meklēšu tīmeklī")

    for i in dati:
        if country == i["name"]["common"]:
            print(f"Valsts {country} ir atrasta, populacija {i["population"]}")
            cur.execute(f"""
                INSERT INTO Valsts (Nosaukums, OficialaisNosaukums, Populacija) VALUES
                ("{i["name"]["common"]}", "{i["name"]["official"]}", {i["population"]})
                """)
            con.commit()
con.commit()
con.close()