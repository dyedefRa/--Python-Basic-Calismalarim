# -*- coding: utf-8 -*-
"""
FAZLA VERI VARSA BUNLA CIZDIRME 
swarmplot aynı anda 3 farklı cesit durumu görselleştirme
Olumsekiilerini görelim ,
Cinsiyete göre 
VE yasa göre 
boxplotun alternatifi gibi dusun 
Tek bir data var.
Bu datanın featurelarını alıyosun (numeric)
ve farklı 3 feature uygulayabılıryosun
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

#boxplota bak daha detaylı anlattım bunları
sns.swarmplot(x='gender',y='age',hue='manner_of_death',data=killData)
plt.show()
