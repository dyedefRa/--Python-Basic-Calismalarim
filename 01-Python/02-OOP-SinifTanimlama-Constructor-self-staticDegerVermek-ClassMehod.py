# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 02:46:02 2018

@author: Baki
"""
#%% self=this gibi sadece ek olarak parametre olarak verıyoruz
#SINIF OLUSTURMAK
#kaç tane nesne üretilmiştir sorsunun cevabı için counter 
#olusturduk onemli olan ;
#Sinifadi.count a +1 demeliyiz her __init__ anında.
# sinif bır tanedır.Nesneye göre +1 dememeliyiz.
class ilksinif:
    sabitZam=1.8
    counter=0
    def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyad=soyisim
        self.maasi=maas
        self.email=isim+soyisim+"@gasg.com"
        ilksinif.counter=ilksinif.counter+1
    def soyisimVer(self,yeniSoyisim):
        self.soyad=yeniSoyisim
    def getAd(self):
        return self.isim
    def sabitineGoreZamArtir(self):
        self.maasi=self.maasi*self.sabitZam
        return f"{self.isim} adlı kişinin yeni maasi = {self.maasi}"

        
    
calisan1=ilksinif("ahmet","korkmaz",1000.00)
calisan2=ilksinif("memo","yilmaz",5555.00)
calisan3=ilksinif("furkan","tan",1400.00)
calisan1.sabitineGoreZamArtir()

listem=[calisan1,calisan2,calisan3]


maximummaas=listem[0].maasi
index=-1
for personel in listem:
     if personel.maasi>maximummaas:
        maximummaas=personel.maasi
        index=personel
      
       
print(index.isim)
print(f"en yuk. maas.= {maximummaas}")
        