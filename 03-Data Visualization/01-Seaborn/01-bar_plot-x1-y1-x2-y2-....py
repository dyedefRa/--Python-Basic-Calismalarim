# -*- coding: utf-8 -*-
#Fatal Police Shootings in the US Datasını kullanacagız
#Visualization= Insanların oranları anlayabılmesı ve etkıleyebılmesı ıcın

# BASLANGIÇ - BIRCOK VERIYI GORSELLESTIRECEGIZ -SORULARIMIZ
#-Read datas
#-Poverty rate of each state
#-Most common 15 Name or Surname of killed People
#-High school graduation rate of the population that is older than 25 in states
#Liseden mezun olma oranları 25 yasından buyuk her eyalette
#Mezun olma oranları vs fakirlik oranı (her eyalette)

# KULLANILACAK PLOTLAR
#Bar Plot | Point | Joint | Count | Pie | Lm | Kde |
#Box | Swarm | Pait Plot
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

#%% Poverty rate of each state - EYALETE GORE YOKSULLUK ORANI (yuksek orandan-dusuge dogru)

#STEP 1 -DATA FIRST LOOK AND DATA RECOVERING(IYILESTIRME)

povertyRateData.head()#=> Not nul diyor. Ama cidden oylemı?
povertyRateData.info()#=> col isimlerine bakalım.
povertyRateData.poverty_rate.value_counts()
#Burada gerçekten yoksuluk oranını degerlerı not nullmı dıye baktık.ve - degerıni gorduk
#- degerıni 0 la degistirelim, replace Kullanarak
povertyRateData.poverty_rate.replace(['-'],0.0,inplace=True)
#degistirdik fakat bu col  object türünde. numbera cevırmelıyız
povertyRateData.poverty_rate=povertyRateData.poverty_rate.astype(float)
#.info() => dersek poverty_rate  29329 non-null float64 olur

#STEP 2 -VERIYI ISTEDIGIMIZ SEKLE GETIRELIM

#Eyaletlere göre yoksulluk oranı alıcaz ve bu buyukten kucuge dogru sıralı olmalı
#each state diyor yani biz burada unique eyaletleri bulmamız gerek.
area_list=list(povertyRateData['Geographic Area'].unique())
area_poverty_ratio=[] #bu list'e for ile arealistte donerkenki sırayla oranları atacagız. Sonra area_list ile bu oranı bır dFrameye atacagız EŞLEŞTIRECEK OTO

for areaName in area_list:
    thatArea=povertyRateData[povertyRateData['Geographic Area']==areaName]#=> Orn:Geo.Are='AL' olanları alıcak
    area_poverty_rate=sum(thatArea.poverty_rate)/len(thatArea) #=> 'AL' aresındakı poverty ratelerı topla ve sayısına bol
    area_poverty_ratio.append(area_poverty_rate)

areaAndRatioData=pd.DataFrame({'area_ismi':area_list,'yoksulluk_orani':area_poverty_ratio}) #=> aynı sırayla bunları bu dataya koyduk
#buyukten kucuge sıralama yapalım (bu olay ozel yanı merdıven seklı olsun dıye)
new_index=(areaAndRatioData['yoksulluk_orani'].sort_values(ascending=False)).index.values#=> sıralayıp ındex aldık
siraliAreaRatio=areaAndRatioData.reindex(new_index)#=> belirli index sırasına gore tekrar ındexler.

#STEP 3 - CIZDIRME OLAYLARI- VISUALIZATION - barplot

plt.figure(figsize=(15,10)) #=> Yeni bir figur aç 15x10 olsun
sns.barplot(x=siraliAreaRatio['area_ismi'],y=siraliAreaRatio['yoksulluk_orani'])
plt.xticks(rotation=45) #=> x'e koydugun verinin adlarını 45 derece cevır.
plt.xlabel('States')
plt.ylabel('Poverty Rate')
plt.title('Poverty Rate of Given States')

#%% AMAC: Oldurulen insanların arasında en çok bulunan 15 isim ve soy isim
killData.head() #=> fikir sahibi olalım ve düzeltmeler yapalım 
killData.info()
killData.name.value_counts() #=> TK TK cıktı bu ne ? Amacım en yaygın ısmı soy ısmı bulmak. Bunu görmezden gelicez .
seperated=killData.name[killData.name!='TK TK'].str.split() #=> TK TK'yı gormezden gelip split ile ayır
#bu seperated verisi 0=> ['Tom','bla'] 1=> ['Jhon','fsaf','kaysafje'] seklinde

soyisimler=[]
for x in seperated:
    soyisimler.append(x[-1])
isimler=[]
ekisimler=[] #=> seperated'ta 3 uzunlukta verim olabılır.ilk indexi buna atacagım 
for a in seperated:
    isimler.append(a[-2])
    if len(a)==3:#=> eger uzunlugu üçse sondan 3. indexli degeri al (yani ilk indexi,umarım 4.indexli deger yoktur :))
        ekisimler.append(a[-3])
        
isim_listem=isimler+ekisimler
name_count=Counter(isim_listem) #=> Bu Counter metodunu kullanmak ııcn collectıon kutuphanesını eklemek gerek
most_common_names=name_count.most_common(15) #=> EN YAYGIN 15 AL ONEMLI

surname_count=Counter(soyisimler)
most_common_surnames=surname_count.most_common(15)
#ilk 15 yaygın degerler için geçerli aşagısı
isim_deger,isim_count=zip(*most_common_names)
isim_deger,isim_count=list(isim_deger),list(isim_count)
soyisim_deger,soyisim_count=zip(*most_common_surnames)
soyisim_deger,soyisim_count=list(soyisim_deger),list(soyisim_count)

#---------------VISUALIZATION
plt.figure(figsize=(15,10)) #=> 15x10 boyutunda bir figure aç hafızada
plt.subplot(2,1,1)
ax=sns.barplot(x=isim_deger,y=isim_count,palette=sns.cubehelix_palette(len(isim_deger)))
plt.xlabel('Name of killed People')
plt.ylabel('Frequency')
plt.title('Most common 15 Name of killed person')

plt.subplot(2,1,2)
ax=sns.barplot(x=soyisim_deger,y=soyisim_count,palette=sns.cubehelix_palette(len(soyisim_deger)))
plt.xlabel('Surname of killed People')
plt.ylabel('Frequency')
plt.title('Most common 15 Surname of killed person')

#%% YATAY BAR PLOT
#Amaç : Eyaletlerdeki ırtkların oranını görselleştir
shareRaceCityData.head()
shareRaceCityData.info() #=> Oranlar object yani string
shareRaceCityData.replace(['-'],0.0,inplace=True)
shareRaceCityData.replace(['(X)'],0.0,inplace=True)
shareRaceCityData.iloc[:,2:7]=shareRaceCityData.iloc[:,2:7].astype(float) #=> float'a çeviridk

eyaletIsimleri=list(shareRaceCityData['Geographic area'].unique()) 
#BURASI ONEMLI UNIQUE EYALET ISIMLERINI ALMAMIZ GEREK EYALETLERE GORE OLD. IICN
#VE BUNU LİSTE CEVIRIYORUZ
share_white=[]
share_black=[]
share_native_american=[]
share_asian=[]
share_hispanic=[]

def oranBulGetir(a):
    return sum(a)/len(a)
    
for i in eyaletIsimleri:#=> Eyalet listesinde gezelım
    x=shareRaceCityData[shareRaceCityData['Geographic area']==i] #'AL' olanlar ıcın 
    share_white.append(oranBulGetir(x['share_white']))
    share_black.append(oranBulGetir(x['share_black']))
    share_native_american.append(oranBulGetir(x['share_native_american']))
    share_asian.append(oranBulGetir(x['share_asian']))
    share_hispanic.append(oranBulGetir(x['share_hispanic']))

#VISUALIZATION
f,ax=plt.subplots(figsize=(9,15))
sns.barplot(x=share_white,y=eyaletIsimleri,color='g',alpha=.5,label='White')
sns.barplot(x=share_black,y=eyaletIsimleri,color='b',alpha=.5,label='African American')
sns.barplot(x=share_native_american,y=eyaletIsimleri,color='cyan',alpha=.5,label='Native American')
sns.barplot(x=share_asian,y=eyaletIsimleri,color='yellow',alpha=.5,label='Asian')
sns.barplot(x=share_hispanic,y=eyaletIsimleri,color='r',alpha=.5,label='Hispanic')

ax.legend(loc='lower right',frameon=True)#=> Legendların görünürlüğü (Orn yeşil çizginin  ne oldugu mavının ne oldugunu yani labelların bırlestıgı yer)
ax.set(xlabel='Percentage of Races',ylabel='States',title="Percentage of State's Population According to Races")
#-----BAR PLOT
#iki liste alıp sırasıyla listelerin 0. indexleri ,1.indexlerini,2.indexlerini
#eş olarak gorup grafigini çizer.1.listin 0. indexinin x e koyduysa 2.listin
#0. indexini y ye koyar bu sekıdle devam eder









