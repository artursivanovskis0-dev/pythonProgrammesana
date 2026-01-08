class iestade():

    def ievade(self):
        self.nosaukums = input("Ievadiet doktorāta nosaukumu: ")
        self.skaits = input("Ievadi pacientu skaitu: ")
        
    def izvade(self):
        print(f"Doktorāts {self.nosaukums} apkalpo {self.skaits} pacientus")

iestade1 = iestade()

iestade1.ievade()
iestade1.izvade()