import random
import time

class auto():
    def __init__(self, modelis, gads):
        self.gads = gads
        self.modelis = modelis
        self.atrums = 0
        self.iedarbinats = False
    
    def start(self):
        if self.iedarbinats == False:
            iespeja = random.randint(1,10)
            if iespeja >= 8:
                print("Nesanāca iedarbināt")
            else:
                self.iedarbinats = True

    def paatrinajums(self):
        if self.iedarbinats == True:
            self.atrums += random.randint(1,5)

class datoraAuto(auto):
    def __init__(self):
        iespejamasMasinas = {"Ford": "1903",
                                "Mercedes-Benz": "1926",
                                "Porsche 356C": "1964",
                                "Rover SD1": "1984",
                                "SSC Ultimate Aero": "2010",
                                "Zenvo TSRS": "2019"}
        pretiniekaMasina, pretMasGads = random.choice(list(iespejamasMasinas.items()))
        self.modelis = pretiniekaMasina
        self.gads = pretMasGads
        self.atrums = 0
        self.iedarbinats = False


print("Ātrs un bez garantijas. 11ID brauciens!")
modelis = input("Ievadi mašīnas modeli: ")
gads = input("Ievadi mašīnas gadu: ")

speletajs = auto(modelis, gads)

dators = datoraAuto()

print(f"Tavs auto: {speletajs.modelis}, ({speletajs.gads})")
print(f"Pretinieka auto: {dators.modelis}, ({dators.gads})")


sakt = input("Lai iedarbinātu mašīnu, spied 1.")
if sakt == "1":
    print(f"Spēlētāja {speletajs.modelis}, ({speletajs.gads}) tiek iedarbināts")
    print(f"Pretinieka {dators.modelis}, ({dators.gads}) tiek iedarbināts")
    speletajs.start()
    dators.start()

    if dators.iedarbinats == False or speletajs.iedarbinats == False:
        print("Kļūme startā! Sacensības nenotiek!")
    else:
        print("Gatavojies!")
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Aiziet!")
        print("Spied Enter, lai uzņemtu ātrumu.")
        sakums = time.time()
        while True:
            enter = input()
            speletajs.paatrinajums()
            dators.paatrinajums()
            print("Spēlētāja ātrums: ", speletajs.atrums, "     Datora ātrums: ", dators.atrums)

            if speletajs.atrums >= 100:
                print("Tu uzvarēji!")
                beigas = time.time()
                print(f'Sacensību laiks: {beigas - sakums:.2f} sekundes')
                break
            elif dators.atrums >= 100:
                print("Tu zaudēji!")
                beigas = time.time()
                print(f'Sacensību laiks: {beigas - sakums:.2f} sekundes')
                break

