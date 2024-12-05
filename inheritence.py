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
    def zam_yap(self,yeni_zam):
        self.maas+=yeni_zam
yonetici=Yonetici("Alakbar",100,"Bilisim departmani")
print(yonetici.bilgilerigosder())
print(yonetici.departman_degistir("Insan qaynaqlari"))
print(yonetici.bilgilerigosder())
print(yonetici.zam_yap(500))
print(yonetici.bilgilerigosder())



