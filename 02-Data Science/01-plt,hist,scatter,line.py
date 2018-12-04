# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 00:36:33 2018

"""
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#=> sns ; visualization kutuphanesi
pokeData=pd.read_csv("pokemon.csv")
pokeData.info()

#%% CORRELATION MAP (ilişki,bağlantı mapi)
#Eger iki feature arasında correlation 1 ise bunlar
#dogru orantılıdır.Yani oda sayisi artarsa ev fiyatıda
#artar.Corr -1 cıkarsa ters orantılı . 0 a yakınsa alakasız seyler.
#yani bir feature ev kirası ıkıncı feature restoran sayısı
pokeData.corr() #=> featureleri karsılastırır birbirine göre dogru ters oran durumu
#cıkarmamıza yarayacak
f,ax=plt.subplots(figsize=(18,18))
sns.heatmap(pokeData.corr(),annot=True,linewidths=.6,fmt=".2f",ax=ax)
#=>rowların birbirleriyle bağıntı durumlarını .corr() ile görduk.Bunu daha gorsel bır hale getırmek ıcın
#heatmap() metodunu kullanyıoruz.
#linewidths= aralık ,fmt=".1f" =>0.0 fmt=".2f"=> 0.00 gibi decimal gosterımı saglar.
#annot=degerlerı gostermeye yarar yani 0.5 0.4 gibi ilişki oranını
#ax i yukarda tanımladık yanı x y oranını 18 18 yaptık kı buyuk olsun yazılar sıgsın vs
#%%BIRKAC TEKRAR
#MathPlotLib => line,scatter and histogram plots.
#Line Plot=> x axsisin zaman ise 
#Scatter=>iki deger arasında correlation var ıse 
#Histogram=> distribution of numeric data lazımsa
#yani bir verinin sayısı yani 80 olan kaçtane var vs

#CUSTOMIZATION => Colors,labels,thickness of line=(linewidth),title
#,opacity,grid,figsize(15,15) buyutur,ticks of axis and linestyle

#ENG thickness of line=kalınlık=linewidth | distribution=dagılım

#%%LINE PLOT -
pokeData.Speed.plot(kind="line",color="g",label="Speed",
                    linewidth=1,alpha=0.5,grid=True,
                    linestyle=":",figsize=(14,14))
pokeData.Defense.plot(color='r',label='Defense',linewidth=1,
                      alpha=0.5,grid=True,linestyle='-.')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='upper right')
plt.title('Line Plots')
plt.show()

#%%SCATTER PLOT - İki valuable arasındaki ilişkiyi bulmamıza yarar
#dogru orantılımı ters mı? (iki verinin birbiri ile dagılımları)
#bir veriyi x e digerini y ye koyarız.

#=> pokeData.plot dedik direk ve feaurelerini parametre içinde verdık
pokeData.plot(kind='scatter',x='Attack',y='Defense',alpha=0.5,
              color='r')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Attack Defense Scatter Plot')
plt.show()

#%% HISTOGRAM PLOT = bir featurenin  degerlerinin tek tek sayılarını
#bulmamıza yarar daha çok.1 feature veririz mantıken.
pokeData.Speed.plot(kind='hist',bins=50,figsize=(15,15))
plt.show()
#kaç tane x hızında pokemon var.  x hızındaki pokemonların
#frekansını verır
#bins= barların sayısı 50 olsun .Aralıkları açki daha net bilgi versin.
#bins yuksek tut.

#Son olarak => 
#plt.clf() #=> hafızadaki grafigi siler .Clean eder.









