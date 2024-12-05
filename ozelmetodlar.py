"""class Kitap():
    pass
kitap=Kitap()
print(kitap)
del kitap
print(kitap)"""
"""class Kitap():
    def __init__(self,isim,yazar,sayifa_sayisi,tur):
        print("Init fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayifa_sayisi=sayifa_sayisi
        self.tur=tur
kitap=Kitap("Istanbul hatirasi","Ahmet Umit",560,"Polisiye")
"""
"""class Kitap():
    def __init__(self,isim,yazar,sayifa_sayisi,tur):
        print("Init fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayifa_sayisi=sayifa_sayisi
        self.tur=tur
    def __str__(self):
        return "Isim: {}\nYazar: {}\nSyfa Sayisi: {}\nTuru: {}".format(self.isim,self.yazar,self.sayifa_sayisi,self.tur)
kitap=Kitap("Istanbul hatirasi","Ahmet Umit",560,"Polisiye")
print(kitap)"""
"""class Kitap():
    def __init__(self,isim,yazar,sayifa_sayisi,tur):
        print("Init fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayifa_sayisi=sayifa_sayisi
        self.tur=tur
    def __str__(self):
        return "Isim: {}\nYazar: {}\nSyfa Sayisi: {}\nTuru: {}".format(self.isim,self.yazar,self.sayifa_sayisi,self.tur)
    def __len__(self):
        return self.sayifa_sayisi
kitap=Kitap("Istanbul hatirasi","Ahmet Umit",560,"Polisiye")
print(len(kitap))"""

class Kitap():
    def __init__(self,isim,yazar,sayifa_sayisi,tur):
        print("Init fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayifa_sayisi=sayifa_sayisi
        self.tur=tur
    def __str__(self):
        return "Isim: {}\nYazar: {}\nSyfa Sayisi: {}\nTuru: {}".format(self.isim,self.yazar,self.sayifa_sayisi,self.tur)
    def __len__(self):
        return self.sayifa_sayisi
    def __del__(self):
        print("Kitap objesi silinir")
kitap=Kitap("Istanbul hatirasi","Ahmet Umit",560,"Polisiye")
del kitap

