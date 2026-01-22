class Gramata():
    nosaukums = "Nav norādīts"
    lppSkaits = 0
    ISBN = "Nav norādīts"
    autors = ""
    zanrs = ""
    izdosanasGads = ""
    pieejamiba = ""

    def __init__(self, nosaukums, lppSkaits, ISBN, autors, zanrs, izdosanasGads, pieejamiba):
        self.nosaukums = nosaukums
        self.lppSkaits = lppSkaits
        self.ISBN = ISBN
        self.autors = autors
        self.zanrs = zanrs
        self.izdosanasGads = izdosanasGads
        self.pieejamiba = pieejamiba
        print("Grāmata ", self.nosaukums, "ir veiksmīgi izveidota")

    def izvadit(self):
        print(f"Grāmatas autors: {self.autors}")
        print(f'Grāmatas nosaukums: "{self.nosaukums}"')
        print(f"Grāmatas izdošanas gads: {self.izdosanasGads}")

    def aprekinat(self, kaveto_dienu_skaits):
        kavejumaMaksa = float(self.lppSkaits * 0.01 * kaveto_dienu_skaits)
        formated = f'{kavejumaMaksa:.2f}'.replace('.', ',')
        
        print(f"Grāmatas {self.nosaukums} kavējuma maksa ir {formated} EUR")

class Fantazija(Gramata):
    def aprekinat(self, kaveto_dienu_skaits):
        kavejumaMaksa = float((self.lppSkaits * 0.01 * kaveto_dienu_skaits)*1.01)
        formated = f'{kavejumaMaksa:.2f}'.replace('.', ',')
        
        print(f"Grāmatas {self.nosaukums} kavējuma maksa ir {formated} EUR")

class GramatuKatalogs():
    def __init__(self):
        self.gramatas = {}
    
    def pievienot(self, gramata):
        self.gramatas.update(gramata)
        print(f"Grāmata {gramata} ir veiksmīgi pievienota.")



epifanijas = Gramata("Epifānijas", 304, "9789934036101", "Imants Ziedonis", "dzeja", "2022", "pieejama")
epifanijas.izvadit()
epifanijas.aprekinat(5)

harijs = Fantazija("Harijs Poters un Filozofu akmens", 223, "9780747532699", "Dž. K. Roulinga", "fantāzija", "1997", "pieejama")
harijs.aprekinat(10)

katalogs = GramatuKatalogs()
katalogs.pievienot(harijs)
katalogs.pievienot(epifanijas)
