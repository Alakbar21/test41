import random
import time
class Kumanda():

    def __init__(self,tv_durum="Kapali",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if(self.tv_durum=="Acik"):
            print("Televziyon aciq.....")
        else:
            print("Televziyon aciliyor....")
            self.tv_durum="Acik"
    def tv_kapat(self):
        if(self.tv_durum=="Kapali"):
            print("Televziyon kapali...")
        else:
            print("Televziyon kapaniyor...")
            self.tv_durum="Kapali"
    def ses_ayarlari(self):
        while(True):
            cevap=input("Sesi azalt: '<'\nSesi artir:'>'\nCixis:exit")
            if(cevap=="<"):
                if(self.tv_ses==0):
                    print("Ses 0 dadir daha da azalmir.")
                else:
                    self.tv_ses-=1
                    print("Ses 1 vahid azaldi\nSes:",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses==31):
                    print("Ses max dadi daha da artmir.")
                else:
                    self.tv_ses+=1
                    print("Ses 1 vahid artdi.\nSes:",self.tv_ses)
            else:
                print("Ses guncellendi.\nSes:",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi...")
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Hazirdaki kanal:",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv drumu:{}\nTv ses:{}\nKanal listesi:{}\nHazidaki kanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


print("""
Televziyon Uygulamasi:
1.Tv ac
2.Tv kapat
3.Ses ayarlari
4.Kanal ekle
5.Kanal sayisini ogrenme
6.Rastgele kanala gecme
7.Televziyon bilgileri
Cixmaq icin 'q' ya basin.
""")
kumanda=Kumanda()
while(True):
    islem=input("Islemi secin:")
    if(islem=="q"):
        print("Proqram sonlandirilir...")
        break
    elif(islem=="1"):
        kumanda.tv_ac()
    elif (islem == "2"):
        kumanda.tv_kapat()
    elif (islem == "3"):
        kumanda.ses_ayarlari()
    elif (islem == "4"):
        kanal_isimleri=input("Kanal isimlerini ',' ile ayirarak girin:")
        kanal_listesi=kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (islem == "5"):
        print(len(kumanda))
    elif(islem=="6"):
        kumanda.rastgele_kanal()
    elif(islem=="7"):
        print(kumanda)
    else:
        print("Yalnis islem girilmis...")



