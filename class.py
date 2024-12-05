"""class Araba():
    model = "Renault Megane"
    renk = "Gumus"
    beygir_gucu = 110
    silindir = 4
Araba1=Araba()
araba2=Araba()
print(Araba1.model)
print(araba2.beygir_gucu)
print(dir(Araba1))"""
"""class Araba():
    model = "Renault Megane"
    renk = "Gumus"
    beygir_gucu = 110
    silindir = 4
    def __init__(self):
        print("init fonkusyon cagrildi")
araba1=Araba()"""
class Araba():
    def __init__(self,model,renk,beygir_gucu,silindir):
        print("Init fonksiyonu cagrildi")
        self.model=model
        self.renk=renk
        self.beygir_gucu=beygir_gucu
        self.silindir=silindir
araba1=Araba("Renault Megan","Gumus",110,4)
araba2=Araba("Peugeot","Beyaz",90,4)
print(araba1.model)
print(araba2.model)




