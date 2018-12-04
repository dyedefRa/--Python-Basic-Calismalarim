#BroadCasting nedir? => Yeni bir feature yaratıp bu feature'ye deger atmak demek
#%% List To Dict | Dict To DataFrame| using Zip which is return Tuple 

import pandas as pd
import matplotlib.pyplot as plt
pokeData=pd.read_csv('pokemon.csv')
country=['Spain','France']
population=['11','15']
list_label=['country','population']
list_col=[country,population]
#Ikı listeyi birleştirebiliyorsun. Tek bir liste yapaıblıyosun.
#ZIP METODU LIST DONER : AMA TUPLE LIST DONER
zipped=list(zip(list_label,list_col))#=> buraya kadarki hepsi list type
#Aynı zmaanda listeyi dict 'e cevırebılıyosun
data_dict=dict(zipped)
dataFrame1=pd.DataFrame(data_dict)
#%%
pokeData.plot(kind='scatter',x='Attack',y='Defense')
pokeData.plot(kind='hist',y='Defense',bins=50,range=(0,500),normed=True)
#range=> 0 dan 500 e kadar olanlar olsun
#normed=> normalize eder .(Soldaki sayılar degıstı) 

#%% Kumulaitf nedir?
fig, axes=plt.subplots(nrows=2,ncols=1)
pokeData.plot(kind='hist',y='Defense',bins=50,range=(0,250),normed=True,ax=axes[0])
pokeData.plot(kind='hist',y='Defense',bins=50,range=(0,250),normed=True,ax=axes[1],cumulative=True)
plt.savefig('cumulatif-savefig.png')
#%% INDEXING PANDAS TIME SERIES @@@@@@*********************

# Stringten DateTime ' a cevirmek=> pd.to_datetime()
datetime_object=pd.to_datetime('1994-05-22')

#Pokemon.head'e yeni bir feature Ekleyelım
date_list=['1996-11-11','1996-11-21','2000-05-11','2000-05-15','2000-06-24']
ilk5Data=pokeData.head()
ilk5Data['datetime']=pd.to_datetime(date_list)

#HER DATANIN INDEXI VARDIR. ISTEDIGIN COL U INDEX OLARAK ATAYABILIRSIN
ilk5Data=ilk5Data.set_index('datetime')

#Bu datam artık time series datadır.Çünkü indexi Datetimedir.
#print(ilk5Data.loc['1752-11-11'])
print(ilk5Data.loc['1996-11-02':'2000-05-14']) #=> ARASINDAKI YILLARI KAPSAYDAN DATALARI GETIR.
#BU SEKILDE CAGIRABILIYORUZ CUNKU INDEXINI DATETIME DEDIGIMIZ FEATUR'U ATADIK.

#RESAMPLING PANDAS TIME SERIES @@@@@*****************************
"""RESAMPLE @ AYA YILA GORE DEGERLERIN DURUMLARI"""
#RESAMPLE yeni bir sample yani row olusturur.
#ORNEK=> Yıllara göre hız ortalamasını getir

ilk5Data.resample('A').mean() #=> datayı RESAMPLE YAP YILA GORE (farklı 2 yıl  var) A=YIL  M=MONTH
ilk5Data.resample('M').mean() #=> AYlara gore yapıyorz bu kez. Farklı 3 ay var
#%%
#EN ERKEN TARIHLE EN SON TARIH ARASINI YAPIYOR TABI ARADAKI BOS DEGERLER BOS KALIYOR.
#Bu degerlerı bazen doldurmamız gerekcek linear olarak=> Yani
#INTERPOLATE METODU =>
ilk5Data.resample('M').first().interpolate('linear')
#Aradaki boş degerlere esit aralık bırakarak dolduruyor.
#Mesela 1.row 5 ise 3.row 9 ise 2. rowa 7 veriyor





