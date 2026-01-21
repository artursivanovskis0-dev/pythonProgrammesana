import csv
with open("agenti.csv", mode = "r", encoding="UTF-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=";")
    filtered = filter(lambda p: 'Izglītības iestāde' == p[0] or "Valsts iestāde" == p[0], spamreader)
    saraksts = []
    for row in filtered:
        print(', '.join(row))
        saraksts.append[row]
    