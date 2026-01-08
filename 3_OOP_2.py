class Skolotajs():
    stunduSkaits = 0
    skolotajaTips = 0
    
    class SakumskolasSkolotajs():
        def __init__(self):
            self.uzvards = input("Ievadi uzvārdu: ")
            self.klase = input("Ievadi skolotaja klasi: ")
            self.stunduSkaits = int(input("Ievadi stundu skatu: "))
            self.skolotajaTips = 1

        # def ievade(self):
        #     self.uzvards = input("Ievadi uzvārdu: ")
        #     self.klase = input("Ievadi skolotaja klasi: ")
        #     self.stunduSkaits = int(input("Ievadi stundu skatu: "))
        #     self.skolotajaTips = 1

        def izvade(self):
            print(f"Sākumskolas (tips- {self.skolotajaTips}) skolotājs {self.uzvards} māca {self.stunduSkaits} {self.klase} klasē.")
            
    class VidusskolasSkolotajs():
        def __init__(self):
             self.uzvards = input("Ievadi vidusskolas skolotaja uzvardu: ")
             self.pirmaisPrieksmets = input("ievadi pirmo prieksmetu: ")
             self.pirmaPrieksmetaStunduSkaits = int(input("ievadi pirma prieksmeta stundu skaitu: "))
             self.otraisPrieksmets = input("ievadi otro prieksmetu: ")
             self.otraPrieksmetaStunduSkaits = int(input("ievadi otra prieksmeta stundu skaitu: "))
             self.skolotajaTips = 3

        # def ievade(self):
        #     self.uzvards = input("Ievadi vidusskolas skolotaja uzvardu: ")
        #     self.pirmaisPrieksmets = input("ievadi pirmo prieksmetu: ")
        #     self.pirmaPrieksmetaStunduSkaits = int(input("ievadi pirma prieksmeta stundu skaitu: "))
        #     self.otraisPrieksmets = input("ievadi otro prieksmetu: ")
        #     self.otraPrieksmetaStunduSkaits = int(input("ievadi otra prieksmeta stundu skaitu: "))
        #     self.skolotajaTips = 3

        def izvade(self):
            kopejaisStSk = self.pirmaPrieksmetaStunduSkaits + self.otraPrieksmetaStunduSkaits
            print(f"Vidusskolas (tips-{self.skolotajaTips}) skolotājs {self.uzvards} māca šādus priekšmetus: {self.pirmaisPrieksmets}, {self.otraisPrieksmets} kopā {kopejaisStSk}")

skolotajs1 = Skolotajs.SakumskolasSkolotajs()
skolotajs2 = Skolotajs.VidusskolasSkolotajs()


skolotajs1.izvade()
skolotajs2.izvade()