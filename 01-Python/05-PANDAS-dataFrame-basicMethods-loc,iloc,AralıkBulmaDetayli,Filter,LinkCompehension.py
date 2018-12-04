# -*- coding: utf-8 -*-

"""
#1) pandas hizli ve etkili for dataframes (List<Object>)
#2) Neden kullanırız? Dosyalar arasında geçişleri kolaydır
#)=>csv ve tct dosylarını acıp gecısler yapabılırız
#3) dataframeslerdeki null veriler için çok koley ve etkili
#4) numpyda reshape yapabiliyoduk pandas daha etkili..
#5) slicing ve indexin kolay. list.Find(x=>x.sss=='') olayi
#6) time series data analizde(zamana bağlı olaylarda) cok yardimci
#7) BU KUTUPHANE COK HIZLI .Optimize edilmiş hızlı!
"""
#%%
import pandas as pd
# bir dic olusturalım ki dataframe olusturabılelım  
sozluk={"name":["ali","veli","kenan","hilal","ayse","evren"],
        "age":[15,12,15,24,15,66],
        "maas":[100,150,244,142,155,675]}

#DataFrame(list alır yada dictionary) , BU BIR TABLODUR**
dataFrame1=pd.DataFrame(sozluk)
#head() => take(5) // DataFramenin ön incelemesi gibi düşün
head1=dataFrame1.head()
# [içine aldıgı parametreye gore ilk nesneleri verir]
#ilk 3ünü al=>
head2=dataFrame1.head(3)
#tail()=> lastTake(5)//Son 5 i al
# [içine aldıgı parametreye gore son nesneleri verir]
tail1=dataFrame1.tail()
#list.OrderByDescanding().Take(x)
#%% pandas basic method
print(dataFrame1.columns) #=>columnlarını ver.
dataFrame1.columns[0] #=>ilk columnu getir
print(dataFrame1.info()) #=>DataFramenin içindeki bilgileri verir
#yani column isimleri tipi nullluk bilgileri hangi framework vs
print(dataFrame1.dtypes)#=>col tiplerini verir sadece
print('--------------')

#=> describe sadece numeric feature(fiçur=özellik)ları alır
#yani col ları alır.Objectleri almaz bu kutuphanede 
#object=string.****************************€€€€

print(dataFrame1.describe())
"""
count=sayisi,mean=ortalama,standartdivesion?,
min,max,50%= medyan degeri,25% 1.quartiali?,75% 3.quartiali
DATASCIENCE DE DETAYLARI OLACAK.
"""
#%% indexin ve slacing olaylari
dataFrame1.columns[0] #=> Sadece 0.indexli feature adını döner

print(dataFrame1["name"])#=> name col(feature)sini doner
print(dataFrame1.name)#=> üsttekiyle aynı kod.
#dataFrame1.name=["e","k","e","e","k","k"] 
#var olan columnbu bu şekilde değiştirebiliytorsun komple.
#--------------
#Yeni feature ekleme olayi (col ekleme) =>
dataFrame1["cinsiyet"]=["e","k","e","e","k","k"] 
"""BURASI ONEMLIII
dataFrame1.loc[:,"name"] => rowların hepsini ve name col unu al
0 1 2 3 rowlarını al ve name col unu al=> 
pandas'ta 0:3=:3= 0 1 2 3 tür !!!!
"""
print(dataFrame1.loc[:3,"name"])
# age'den nameye kadar olanları yazdır ve tum rowları al
print(dataFrame1.loc[:,"age":"name"])

""" BURASI DA ONEMLI ******************** """
# 1 ve 3 rowlu 2 ve 4 col lu dataları getir
print(dataFrame1.loc[[1,3],["maas","cinsiyet"]])
print('***Tersten yazdırma')
#Ters olark listi getir. OrderByDescanding=>
print(dataFrame1.loc[::-1,:])

#Tüm satırları yazdır ama col olarak nameye kadar olanları getir
print(dataFrame1.loc[:,:"name"])

#COL ları belırlemek için illa col name bilmek zorunda degılız
#indexe göre almak için =>
print('Colları indexle çağırmak =>>iloc **')
print(dataFrame1.iloc[:,0:3])
print(dataFrame1.iloc[:,[0,3]])
#%% filtering
# maasi 200lira ve üstü olanları bulalım
filtre1=dataFrame1.maas>200 #=> true false olarak getırıyor
filtrelenmis1=dataFrame1[dataFrame1.maas>200]
#=> yada filtrelenmis1=dataFrame1[filtre1]
filtre2=dataFrame1.age<25
#=> hem maas>200 hemde age<25
filtrelenmis2=dataFrame1[filtre1 & filtre2]

#%% List comprehension =LINQ EXPRESS GIBI DUSUN
#dataFramedeki maas col un ortalamasını bulalım

#import numpy as np
#ortmaasNP=np.mean(dataFrame1.maas)
print('----ONEMLII-----')
#=> colların ısmnı buyuklestır
dataFrame1.columns=[col.upper()  for col in dataFrame1.columns]
ortdeger=dataFrame1.MAAS.mean()
#=> AMAC: ort altlı maaslılılara dusuk,ort ustlulere yuksek maaslı
#maaslı yazan yenı bır col(feature) eklıcez
dataFrame1["maas Durumu"]=["yuksek" if ortdeger<obj else "dusuk" for obj in dataFrame1.MAAS]



#=>bosluklu olan veriler varsa boşluk yerine _ yap
dataFrame1.columns=[obj.split()[0]+"_"+obj.split()[1] if len(obj.split())>1 else obj for obj in dataFrame1.columns]

#=> if kullandıysan list comprehensionda else de kullanacaksın
#return olayina ıyı bak...Yani bu list zımbırtıları aslında.
# List.Where.  List.Select gibi
#%% DROP OLAYLARI
#=>axis'i 1 olan (yani col)
#,inplace=True parametresi return olarak degistirir.
dataFrame1.drop(['maas_Durumu'],axis=1)
dataFrame1.drop(0)
#---------
d1=dataFrame1.head()
d2=dataFrame1.tail()
# vertical birleştirelim=>
d_concatv=pd.concat([d1,d2],axis=0)#=> axis=0 rowla ılgılıdır. asagı dogru tabloları bırlestırır
d_concath=pd.concat([d1,d2],axis=1)
maas=dataFrame1.MAAS
yas=dataFrame1.AGE
d_concatmy=pd.concat([maas,yas],axis=1)
print(d_concatmy)
#%% TRASNFORMING DATA

dataFrame1["maasx2"]=[a*2 for a in dataFrame1.MAAS]

#apply()=>
def ikile(yas):
    return yas*2

dataFrame1["apply_metodu"]=dataFrame1.MAAS.apply(ikile)




#%% 

"""
OZEL BENIM YAPTIKLARIM 
"""

liste={"ad":["Korkusuzlar","Elon Musk","Death Note","Pucca Gunlugu","KayıpGül"],
       "basim Yili":[1996,1994,1994,2005,2003],
       "ucret":[55,25,66,22,44]}
#sozluk={"name":["ali","veli","kenan","hilal","ayse","evren"],
#        "age":[15,12,15,24,15,66],
#        "maas":[100,150,244,142,155,675]}
dataFrame1=pd.DataFrame(liste)
dataFrame1.head(2) #=> Take(2)
dataFrame1.tail(2) #Son(2)
dataFrame1.columns
dataFrame1.dtypes
dataFrame1.describe()
#dataFrame1["ad"]
##=> coloumb 'ad' oalni donder
#dataFrame1.ad
dataFrame1.iloc[:,0:2]
dataFrame1.iloc[[1,3],[0,2]]#=> nokta atsıı ıcın [] gerek. aralık ıcın : gerek.
dataFrame1.iloc[:3,[0,2]]
#%%
#filtre1=dataFrame1.basimYili<2003
#filtre2=dataFrame1.ucret>50
#fil1=dataFrame1.filter(filtre1 & filtre2)
#------------
#ucretOrt=dataFrame1.ucret.mean()
#dataFrame1["maasDurumu"] =["yuksek" if a>ucretOrt else "dusuk" for a in dataFrame1.ucret]

#------------
dataFrame1.columns=[a.upper() for a in dataFrame1.columns]

dataFrame1.columns=[a.split()[0]+'_'+a.split()[1] if len(a.split())>1 else a for a in dataFrame1.columns]













