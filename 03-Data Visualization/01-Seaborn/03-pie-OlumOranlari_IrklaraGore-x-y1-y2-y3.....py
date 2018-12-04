# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 02:28:23 2018

Bir x degerini y1,y2,y3,y4 degerlerıne oranlarken bunu kullanırız.
Yani olum oranının ırklara gore dagılımını pie ıle yaparız

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

#AMAC OLDURULEN INSANLARIN IRKLARA GORE ORANI

killData.head()
killData.race.value_counts() # => 0 olan diger(others) ırklar.
#Eger boş bir data varsa bunu datadan cıkartacagız
#cunku ıstenılen Race'yi almamız gerekıyor.Boş bır ırk varsa 0 yapamayacagımız için
#Replace yapamayacagımız ıcın bunu datadan cıkartmak daha mantıklı
killData.race.dropna(inplace=True)#=> Boş Dataları cıkart

irk_isimleri=killData.race.value_counts().index
colors=['grey','blue','red','yellow','green','brown'] #=> ırkların cesit sayısına gore renk cesıdı
explode=[0,0,0,0,0,0]#=> piechart'ın oranları olacak bunları dolduracagım daha sonra
irkOlumSayilari=killData.race.value_counts().values
#=> ilk param=> 1200,500,300 | 2=> White,Black |3=> colors
plt.figure(figsize=(7,7))
plt.pie(irkOlumSayilari,labels=irk_isimleri,colors=colors,autopct='%1.1f%%') #=> autopct= 1 tane ondalık kısım goster dıyoruz
plt.title('Killed People According to Races',color='blue',fontsize=15)

#OTO OLARAK ORANLARI BULUP ORANLIYOR.






