# -*- coding: utf-8 -*-
"""
Unclean data nasıl olur?
1-Column isimlerinde
 upper-lower problemleri(hepsi kucuk olsa iyi olur)
 Spacing words =-Bosluk olmasın .
2-Missing Data
 Datalarda boşluk olması
3-Different Language
 Farklı dilden veriler olmasın

"""
#%%
import pandas as pd
pokeData=pd.read_csv('pokemon.csv')

print(pokeData.shape) #=> 800,12 (800 row,12 col=feature)
print(pokeData.info()) #=> 
#%% EXPLOTARY DATA ANALYSIS (EDA)

#1- value_count()
#pokemon.csv için ele alırsak bu datada 'Type 1' adında feature var
#bu featureların degerlerinin countlarını almak istersek
#.value_count() KULLANIRIZ
valueCountForType1=pokeData['Type 1'].value_counts()
#=> 800 tane veri içinde Type 1'i water olan blalba ,Fire olan blalba tane veri varmış
#%%
"""
#@Median(Quartile) nedir?
#-Ortadaki sayıdır.
#1,4,5,6,8,9,11,12,13,14,15,16,17 için=>
#11 mediandır(quartile)

#@lower quartile nedir? => en kucuk deger ile quartile'ın ortasıdır
#=> 6 is lower quartile
#Aynı zamanda Q1 denir .Yada 25% Quartile da denir *********

#upper quartile nedir? => en buyuk deger ile medyan arasındaki medyan(ortadaki sayi)
#=>14 is upper quartile => 14=Q3 => 14 = 75% Quartile 

#2- outliers =ayrık ,aykırı demek @@@@@@@@@@@@@
#Bir datadaki çok yuksek yada çok düşük degerler.
#Peki bu yukseklık dusukluk neye göre?
#Q3 ile Q1 arasındaki farka = IQR denilir.
#Q1-IQR*1,5 degerinin altındaki degerler outliersdir
#Q3 +IQE*1,5 dan buyuk deger yine outliersdır
"""
#%%VISUAL EXPLORATORY DATA ANALYSIS (VEDA)

print('BURASI ONEMLI!! Q1 Q2 Q3 quartiersları ve outliers')
#1-Box plots= outliersları,min,max,quartiers'ları visualize eder
pokeData.boxplot(column='Attack',by='Legendary')
#Legendary durumuna göre Attack featurenin Q1,Q2,Q3 ve outlierslarının visiualizesini yap

#%% 1-TIDY DATA
#Datamı melt etmek istiyorum
#Datadan  belirli featureleri secerek yeni bir data olusturma olayı
data_new=pokeData.head()
meltlenmis=pd.melt(frame=data_new,id_vars='Name',
                   value_vars=['Attack','Defense'])
meltlenmis 
#=>verdigim datanın id olarak belirtigm feature'ına gore(Degişmeden kalsın dedik buna)
#Attack ve Defans degerleri yaz
#ID|variable|value olacak sadece datada feature olarak!

#2-PIVOTING DATA
#melted datayı eski halıne cevırır
meltlenmis.pivot(index='Name',columns='variable',values='value')

#%% CONCATENATING DATA
#Data birleştirilmesi
data1=pokeData.head()
data2=pokeData.tail()
v_concat_data=pd.concat([data1,data2],axis=0,ignore_index=True)
#axis=0 Vertical,axis=1 Horizontal Birleştir(yanyana) demek
#ignore_index=True => indexleri boşver yeni index ata
h_concat_data=pd.concat([data1['Attack'],data1['Defense']],axis=1)

#Topluca bir featuren type'ını degıstırme olayı=> 
print(pokeData.dtypes)
pokeData['Type 1']=pokeData['Type 1'].astype('category')
pokeData['Speed']=pokeData['Speed'].astype('float')
print(pokeData.dtypes)

#%% MISSING DATA and TESTING WITH ASSERT
#Boş veriyle karşılaştığımızda ne yaparız?
#-onu oylece bırakbılırsın
#-missing valueları datasetten cıkartabılırız
#-fillna() ile missing valueları Non ile doldurabılırız
#-Sayısal degerler ıcın medyanı ıle doldurabılırsın.

pokeData.info()

pokeData['Legendary'].value_counts()
#=> Legendaryin degerlerine gore sayılarını verır
pokeData['Type 2'].value_counts(dropna=False)
#Type 2 nin degerline gore sayısını ver. Non olanlarıda al


pokeData['Type 2'].dropna(inplace=True)

#Assert iki degerin aynı/eşit olup olmadıgına bakar 
#aynıysa hata donmez.Farklıysa hata doner.
assert 1==1    #=> RETURN NOTHING
#assert 1==2   #=> RETURN ERROR

assert pokeData['Type 2'].notnull().all()

#Null olanları Empty yazdıralım
pokeData['Type 2'].fillna('empty',inplace=True)

#%% assert'i bşka nerede kullanırız?
#olayı su ,iki degerin equal olup olmamasına bakıyor
import numpy as np
assert pokeData.columns[1]=='Name' 
assert pokeData.Speed.dtypes==np.int64






