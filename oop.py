from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, vards, uzvards):
        self.vards = vards
        self.uzvards = uzvards
    @abstractmethod
    def statiesPrieksa(self):
        pass
        #return f"Mani sauc {self.vards} {self.uzvards}"

class Skolens(Persona):
    def __init__(self, klase, vards,uzvards):
         self.klase = klase
         super().__init__(vards, uzvards)
    def statiesPrieksa(self):
        print(f"Mani sauc {self.vards} {self.uzvards}, eju {self.klase}. klasē")

class Skolotajs(Persona):
    def __init__(self, prieksmets, vards, uzvards):
        self.prieksmets = prieksmets
        super().__init__(vards, uzvards)

    def statiesPrieksa(self):
        print(f"Mani sauc {self.vards} {self.uzvards}, mācu {self.prieksmets} ")

s1 = Skolens("12.ID","Juris","Bērziņš")
s2 = Skolotajs("Matemātika", "Jānis", "Skalbe")
s1.statiesPrieksa()
s2.statiesPrieksa()