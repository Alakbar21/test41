class Hayvan():
    def __init__(self,isim="jiti",yas=5,ayaq_sayi=4):
        self.isim=isim
        self.yas=yas
        self.ayaq_sayi=ayaq_sayi
    def bilgilerigosder(self):
        print("Hayvanin ismi:{}\nHayvanin yasi:{}\nHayvanlarin ayaq sayi:{}".format(self.isim,self.yas,self.ayaq_sayi))
class Kopek(Hayvan):
    def __init__(self,isim,yas,ayaq_sayi,gidalanmasi):
        super().__init__(isim,yas,ayaq_sayi)
        self.gidalanmasi=gidalanmasi
    def bilgilerigosder(self):
        print("Kopekin ismi:{}\nKopekin yasi:{}\nKopekin ayaq sayi:{}\nKopekin qidalanmasi:{}".format(self.isim,self.yas,self.ayaq_sayi,self.gidalanmasi))

it=Kopek("jj",5,4,"yem")
it1=Hayvan()
print(it1.bilgilerigosder())

