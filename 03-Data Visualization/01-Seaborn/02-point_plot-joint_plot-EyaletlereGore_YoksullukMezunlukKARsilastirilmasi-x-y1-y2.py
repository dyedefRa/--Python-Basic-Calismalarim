# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 00:20:45 2018
POINT VE  JOINT PLOT
ve bu plotları uygulamak ıcın aynı x e sahip farklı y1,y2 oranları olması gerek ve ben
bu y1 y2 yi karşılastırmak ıstedıgımde kullanırız.
yani area_list,yoksulluk_orani | area_list,mezunıyet_durumu gibi
VEE DAHA ONEMLIIS
 normalization ile  y1,y2 verilerini aynı dereceye cekmem gerek
 bunun içinde y1=y1/max(y1) ve y2=y2/max(y2) 
 demelisin.

"""
#%% GENEL KUTUPHANE VE CSV UZANTILAR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import collections
from collections import Counter #=> 2.ornekte Counter kullanmak ıcın


incommonData=pd.read_csv('csv/MedianHouseholdIncome2015.csv',encoding="windows-1252")
povertyRateData=pd.read_csv('csv/PercentagePeopleBelowPovertyLevel.csv',encoding="windows-1252")
highSchoolComplete25Data=pd.read_csv('csv/PercentOver25CompletedHighSchool.csv',encoding="windows-1252")
shareRaceCityData=pd.read_csv('csv/ShareRaceByCity.csv',encoding="windows-1252")
killData=pd.read_csv('csv/PoliceKillingsUS.csv',encoding="windows-1252")

#%% Her bir eyalet için liseden mezun olma oranı ve fakirlik oranı

povertyRateData.info()
povertyRateData.poverty_rate.value_counts()
#=> - var bunu 0 a cevır ve objecgi float yap
povertyRateData.poverty_rate.replace(['-'],0.0,inplace=True)
povertyRateData.poverty_rate=povertyRateData.poverty_rate.astype(float)
#Aynı sekılde mezunolma datasındada degısıklık yapalım
highSchoolComplete25Data.percent_completed_hs.replace(['-'],0.0,inplace=True)
highSchoolComplete25Data.percent_completed_hs=highSchoolComplete25Data.percent_completed_hs.astype(float)
#Eyalet isimlerini alalım
eyalet_isimleri=list(povertyRateData['Geographic Area'].unique())
yoksulluk_orani=[]
mezunolma_orani=[]
def oranBul(k):
    return sum(k)/len(k)

for i in eyalet_isimleri:
    yoksullukNesnesi=povertyRateData[povertyRateData['Geographic Area']==i]
    yoksulluk_orani.append(oranBul(yoksullukNesnesi['poverty_rate']))
    mezunOlmaNesnesi=highSchoolComplete25Data[highSchoolComplete25Data['Geographic Area']==i]
    mezunolma_orani.append(oranBul(mezunOlmaNesnesi['percent_completed_hs']))
    
#SIRALAMA YAPALIM AYRI AYRI
area_yoksullukData=pd.DataFrame({'area_list':eyalet_isimleri,'yoksulluk_oranlari':yoksulluk_orani})
area_mezuniyetData=pd.DataFrame({'area-list':eyalet_isimleri,'mezunolma_oranlari':mezunolma_orani})
#new_index_yoksulluk=area_yoksullukData['yoksulluk_oranlari'].sort_values(ascending=True).index.values
#new_index_mezuniyet=area_mezuniyetData['mezunolma_oranlari'].sort_values(ascending=True).index.values
#sorted_yoksulluk=area_yoksullukData.reindex(new_index_yoksulluk)
#sorted_mezuniyet=area_mezuniyetData.reindex(new_index_mezuniyet)

""" *************************
 POINT PLOT aynı x'e sahip farklı iki y1,y2 verinin
aynı dataya alınarak (3 col yaparak concat ile)
BIRBIRIYLE KARSILASTIRMASINDA ISIMIZE YARAR
"""
#Normalization. İki veriyi birbiriyle karsılastırmak istyıoruz.
#x ekseni için AL,NY ...
#y1=[1,2,3,4]
#y2=[100,214,515,525] olsun. Ben y1 ile y2 yı karsılastırmak ıstedıgımde.
#Normalızatıon yaparım. yani aynı anda bunları bu sekılde yaptıgımda
#y1 in  degisimi pek bellı olmayacak O yuzden normalization yapmalyıız.=>
def normalizationYap(listOran):
    return listOran/max(listOran)
#=> her orani maximumuna bolersek aradakı y1 ıle y2 yı aynı dereceye getırırz.
    
area_yoksullukData['yoksulluk_oranlari']=normalizationYap(area_yoksullukData['yoksulluk_oranlari'])
area_mezuniyetData['mezunolma_oranlari']=normalizationYap(area_mezuniyetData['mezunolma_oranlari'])
concatedData=pd.concat([area_yoksullukData,area_mezuniyetData['mezunolma_oranlari']],axis=1) #=> col olarak birleştir
concatedData.sort_values('yoksulluk_oranlari',inplace=True)

#VISUALIZATON -POINTPLOT( data PARAMETRESI VAR)

f,ax1=plt.subplots(figsize=(20,10))
#ConcatedData yı veriyoruz data olarak
sns.pointplot(x='area_list',y='yoksulluk_oranlari',data=concatedData,color='lime',alpha=0.8)
sns.pointplot(x='area_list',y='mezunolma_oranlari',data=concatedData,color='red',alpha=0.8)
plt.text(40,0.6,'Yüksek okul mezun oranı',color='red',fontsize=17,style='italic') #=> 40,06 felan kordinat olarak texti yazdıracagımz yer.
plt.text(40,0.55,'Yoksulluk oranı',color='lime',fontsize=18,style='italic')
plt.text(44,0.50,'Baki Öztürk',color='cyan',fontsize=12,style='italic')
plt.xlabel('Eyaletler',fontsize=15,color='blue')
plt.ylabel('Degerler',fontsize=15,color='blue')
plt.title('Yuksek Okul Mezun Oranı | Yoksulluk Oranı Karşılaştırılması',fontsize=20,color='blue')
plt.grid() #=> ızgarayı gostersın.

#%% JOINT PLOT  SORUMUZ AYNI MEZUNIYET ILE YOKSULLUGU KARSILASTIR DENILIYOR =kdeplot la  aynı cunku kind='kde' dedık

concatedData.head()

g=sns.jointplot(concatedData.yoksulluk_oranlari,concatedData.mezunolma_oranlari,kind='kde',size=7)
#=> size=7 plotun büyüklügü. figsize gibi birşey
#=> kind ='kde' kernel desity estimation.

#GRAFIGI CIZDIRDIGINDE ;
#1-pearsonr=-0.81 diye bir deger var
#pearsonR , corralationu gosterir. -1'e cok yakın oldugu için
#ters orantiya yakın dıyebılırız
#2-grafigin dısında mavi yerler var
#bunlar kde'dır.Bunların pdf olarak da dusunebılırz.(probablity density function)

#%%
""" FARKLI JOINT PLOT ORNEKLERI """
#PROBLEM HALA AYNI OLSUN
g=sns.jointplot('yoksulluk_oranlari','mezunolma_oranlari',data=concatedData,size=5,ratio=3,color='r')