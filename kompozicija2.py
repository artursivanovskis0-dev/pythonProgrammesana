class darbiba():
    def __init__(self):
        self.info = ""
    def ieslegt(self):
        print(self.info, "Ieslēgts")
    def izslegt(self):
        print(self.info, "Izslēgts")

class RAM(darbiba):
    def __init__(self):
        self.info = "HyperX DDR5 5600 mhz 32GB"

class CPU(darbiba):
    def __init__(self):
        self.info = "Intel 12900k 3.2GHz"

class POWER(darbiba):
    pass

class GPU(darbiba):
    def __init__(self):
        self.info = "Nvidia GeForce RTX 5090"

class PC():
    def __init__(self):
        self.RAM = RAM()
        self.CPU = CPU()
        self.POWER = POWER()
        self.GPU = GPU()
        self.komponentes = [self.RAM, self.CPU, self.POWER, self.GPU]

    def ieslegtDator(self):
        print("Ieslēdz datoru!")
        for komponente in self.komponentes:
            komponente.ieslegt()

    def izslegtDator(self):
        print("Izslēdz datoru!")
        for komponente in self.komponentes:
            komponente.izslegt()


dators = PC()
dators.ieslegtDator()
dators.izslegtDator()