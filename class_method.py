class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def bilgilerigosder(self):
        print(""" 
        Yazilimci objesinin ozellikleri
        Isim:{}
        Soyisim:{}
        Numara:{}
        Maas:{}
        Bildigi Diller:{}
        """.format(self.isim, self.soyisim,self.numara,self.maas,self.diller))
    def zam_yap(self,zam_miqdari):
        print("Zam ediliyor")
        self.maas+=zam_miqdari
    def dil_ekle(self,yeni_dil):
        print("dil ekleniyor")
        self.diller.append(yeni_dil)
yazilimci=Yazilimci("Mustafa Murat","Coskun",12345,3000,["python","java","c","Javascript"])
print(yazilimci.bilgilerigosder())
print(yazilimci.zam_yap(12))
print(yazilimci.dil_ekle("go"))
print(yazilimci.bilgilerigosder())
