class Gramata():
    def __init__(self, autors, zanrs, nosaukums):
        self.autors = autors
        self.zanrs = zanrs
        self.nosaukums = nosaukums

    def __str__(self):
        return f'Autors: {self.autors}, Nosaukums: "{self.nosaukums}", Žanrs: {self.zanrs}'

class Biblioteka():
    def __init__(self):
        self.gramata1 = Gramata("Bobs", "Romans", "Boba piedzivojumi")
        self.gramata2 = Gramata("Harijs", "Romans", "Harija piedzivojumi")
        self.gramatas = [self.gramata1, self.gramata2]

    def apskatitGramatas(self):
        print("--------------Pieejamās grāmatas--------------")
        for gramata in self.gramatas:
            print(gramata)
        print("------------------------------------------")

    def atrastGramatu(self, gNosaukums):
        for gramata in self.gramatas:
            if gNosaukums == gramata.nosaukums:
                return print(f'Grāmata "{gNosaukums}" tika atrasta')
            
        print(f'Grāmata "{gNosaukums}" netika atrasta')

    def iznemtGramatu(self, gNosaukums):
        for gramata in self.gramatas:
            if gNosaukums == gramata.nosaukums:
                self.gramatas.remove(gramata)
                return print(f'Grāmata "{gNosaukums}" tiek iznemta')
            
        print(f'Grāmata "{gNosaukums}" netika atrasta')

    def pievienotGramatas(self, gAutors, gZanrs, gNosaukums):
        jaunaGramata = Gramata(gAutors, gZanrs, gNosaukums)
        self.gramatas.append(jaunaGramata)
        print(f'Grāmata {jaunaGramata.nosaukums} pievienota')


b1 = Biblioteka()
b1.apskatitGramatas()

b1.atrastGramatu("Pētera piedzīvojumi")
b1.atrastGramatu("Harija piedzivojumi")

b1.iznemtGramatu("Boba piedzivojumi")
b1.apskatitGramatas()

b1.pievienotGramatas("Arturs", "Novele", "Artura piedzivojumi")
b1.pievienotGramatas("Didars", "Stāsts", "Didara piedzivojumi")
b1.apskatitGramatas()