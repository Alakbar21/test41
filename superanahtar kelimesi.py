class Calisan():
    def __init__(self,isim,maas,departman):
        print("Calisan sinifinin init fonksuyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgilerigosder(self):
        print("Calisan sinifinin bilgileri....")
        print("""
        Isim:{}
        Maas:{}
        Departman:{}
        """.format(self.isim,self.maas,self.departman))
    def departman_degistir(self,yeni_departmanismi):
        self.departman=yeni_departmanismi
class  Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        super().__init__(isim,maas,departman)
        print("Yonetici sinif inif fonksiyonu")

        self.kisi_sayisi=kisi_sayisi

    def bilgilerigosder(self):
        print("Yonetici sinifinin bilgileri....")
        print("""
        Isim:{}
        Maas:{}
        Departman:{}
        Kisi sayi:{}
        """.format(self.isim, self.maas, self.departman,self.kisi_sayisi))

    def zam_yap(self,yeni_zam):
        self.maas+=yeni_zam
yonetici=Yonetici("Alakbar",3500,"Bilisim",5)
print(yonetici.bilgilerigosder())