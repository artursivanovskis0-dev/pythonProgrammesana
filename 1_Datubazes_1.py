import sqlite3

con = sqlite3.connect("Eksamens.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Kafejnicas(ID INTEGER PRIMARY KEY AUTOINCREMENT, Nosaukums VARCHAR, Adrese VARCHAR)")

cur.execute("CREATE TABLE IF NOT EXISTS Darbinieki(ID INTEGER PRIMARY KEY AUTOINCREMENT,Vards VARCHAR, Uzvards VARCHAR, TelNr VARCHAR, Amats VARCHAR, KafejnicaKuraStrada INTEGER FOREIGN KEY REFRENCES Kafejnicas(ID), AtvalinajumaStatuss VARCHAR)")

cur.execute("CREATE TABLE IF NOT EXISTS Pasutijums(ID INTEGER PRIMARY KEY AUTOINCREMENT, Summa MONEY, Datums DATE, Apraksts VARCHAR, PasutitajsID INTEGER FOREIGN KEY REFRENCES Darbinieki(ID))")

cur.execute(f"""
            INSERT INTO History (Country, Universities) VALUES
            ()
            """)

con.commit()
con.close()