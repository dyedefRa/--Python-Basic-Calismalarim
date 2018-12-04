# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 00:52:23 2018
AMAC:
1-Olen insanlarin F-M sayilari
2-Silah çeşitlerine göre ölüm sayıları
3- Yaşı 25ten küçük/Büyük olanların sayıları
4-Irklara gore olum sayıları
Bu sayi olaylarını Visualization ypamaya yarar
"""
#%% GENEL KUTUPHANELER VE CSV

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

killData=pd.read_csv('csv/PoliceKillingsUS.csv',encoding="windows-1252")

killData.head()
killData.info()

killData.gender.value_counts()
#M=2428  F 107 bunu görsellestirelim
sns.countplot(killData.gender)
plt.title('gender',color='r',fontsize=5)

killData.armed.value_counts()
 #=> bir suru farklı data varmıs gorsellestırelım
#%% Burada silah  ceşitlerine gore olum sayısı dedıgımızde x1,x2,x3,x4,y1 vs..
plt.figure(figsize=(101,7))
#plt.xticks(rotation=90) 
#sns.countplot(killData.armed) #=> bu cok saglıklı olmadı

armed=killData.armed.value_counts()
sns.barplot(x=armed[:7].index,y=armed[:7].values)
plt.ylabel('Number of Death')
plt.xlabel('Wapon Types')
plt.title('Kill Weapon',color='b',fontsize=15)

#%% 25yasından buyuk olan ve olmayanları sayılarını

filte1=['above25' if i>=25 else 'below25' for i in killData.age]
dataframe1=pd.DataFrame({'age':filte1})

sns.countplot(x=dataframe1.age)
plt.ylabel('Number of Killed People')
plt.xlabel('Age of Killed People',color='blue',fontsize=15)
plt.show()
#%% Irklara gore olum sayiları

sns.countplot(data=killData,x='race')

#%% EN TEHLIKELI SEHIRLER

city=killData.city.value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x=city[:12].index,y=city[:12].values) #=> ilk 12 veriyi al dıyoz
plt.xticks(rotation=45)
plt.title('Most dangerous cities',color='r',fontsize=15)







