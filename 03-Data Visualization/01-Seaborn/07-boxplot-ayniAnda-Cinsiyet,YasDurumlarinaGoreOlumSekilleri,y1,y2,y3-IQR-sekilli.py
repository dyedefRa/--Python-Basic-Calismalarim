# -*- coding: utf-8 -*-
"""
boxplot aynı anda 3 farklı cesit durumu görselleştirme
Olumsekiilerini görelim ,
Cinsiyete göre 
VE yasa göre
"""
#%% GENEL KUTUPHANELER VE CSV

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

incommonData=pd.read_csv('csv/MedianHouseholdIncome2015.csv',encoding="windows-1252")
povertyRateData=pd.read_csv('csv/PercentagePeopleBelowPovertyLevel.csv',encoding="windows-1252")
highSchoolComplete25Data=pd.read_csv('csv/PercentOver25CompletedHighSchool.csv',encoding="windows-1252")
shareRaceCityData=pd.read_csv('csv/ShareRaceByCity.csv',encoding="windows-1252")
killData=pd.read_csv('csv/PoliceKillingsUS.csv',encoding="windows-1252")

killData.head()
killData.info()

# Birden cok grafik aynı anda olacagı ıcın tıpkı violin plottaki gibi PALET OLACAK

sns.boxplot(x='gender',y='age',hue='manner_of_death',data=killData,palette='PRGn')
#=> x için => gender'a gidiyor uniqueleri buluyor 'M' ve 'F' buldu x i ikiye ayırıyor.
# y için yine unique buluyor ve aralıkları buluyor
#hue=> 'manner_of_death' e git uniqueleri bul ve x'in ayrıldıgı kadar grafigi bir de hue'nin uniqueleri kadar ayır.
#manner_of_death=> olum sekıllerı
plt.show()