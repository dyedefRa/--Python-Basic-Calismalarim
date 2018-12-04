
"""
sns.heatmap =>data.corr() 'u visualization yapmamızı saglar
 data.corr() metodunu parametre olarak alıyor.
 Ayrıca data.corr() metodu verilien datanın numeric degerlerini 
 corelasyon yaparak sana bir tablo verir.
 
AMAC: Fakirlik oranı ıle Yoksulluk oranının korelasyonu

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

#Amac icin gerekli olan kutuphaneler=> poverty.. ve high....
#DATA IYILESTIRME
povertyRateData.head()
povertyRateData.info() #=> poverty rate onject turunde . bunu float'a cevırelım Tabi ondan önce boş degerleri dolduralım
povertyRateData.poverty_rate.value_counts()
povertyRateData.poverty_rate.replace(['-'],0.0,inplace=True) #=> ONCE BUNU YAP CUNKU - ISARETI objectten Floata (astype yapamazsın) cevıremezsın.
povertyRateData.poverty_rate=povertyRateData.poverty_rate.astype(float)

highSchoolComplete25Data.info()
highSchoolComplete25Data.percent_completed_hs.value_counts()
highSchoolComplete25Data.percent_completed_hs.replace(['-'],0.0,inplace=True)
highSchoolComplete25Data.percent_completed_hs=highSchoolComplete25Data.percent_completed_hs.astype(float)

eyalet_isimleri=list(povertyRateData['Geographic Area'].value_counts().index)
eyalet_yoksulluk=[]
eyalet_mezunluk=[]

def oraniBul(x_eyaleti):
    return sum(x_eyaleti)/len(x_eyaleti)

def normalizasyonYap(x_feature):
    return x_feature/max(x_feature)

for i in eyalet_isimleri:
   yoksullukNesnesi= povertyRateData[povertyRateData['Geographic Area']==i] #=> 'AL' olan yoksullukNesnesi.
   mezunlukNesnesi=highSchoolComplete25Data[highSchoolComplete25Data['Geographic Area']==i]
   eyalet_yoksulluk.append(oraniBul(yoksullukNesnesi.poverty_rate))
   eyalet_mezunluk.append(oraniBul(mezunlukNesnesi.percent_completed_hs))


topluData=pd.DataFrame({'eyalet':eyalet_isimleri,'yoksulluk_orani':eyalet_yoksulluk,'mezuniyet_orani':eyalet_mezunluk})
#NORMALIZASYON =>
topluData.yoksulluk_orani=normalizasyonYap(topluData.yoksulluk_orani)
topluData.mezuniyet_orani=normalizasyonYap(topluData.mezuniyet_orani)

#=> yoksulluk_orani'na göre yeniden sırala
topluData.sort_values('yoksulluk_orani',inplace=True)


#VISUALIZATION
#Corelation'a bakalım nasılmıs
topluData.corr() #=> bu metod datanin numeric degerleri arasındakı ılıskıyı bulur
# corelasyon 1 çıkarsa dogru orantı| -1 ıse ters | 0 ıse alakasız

f,ax=plt.subplots(figsize=(5,5))
sns.heatmap(topluData.corr(),annot=True,linewidths=.5,linecolor='r',fmt='.1f',ax=ax)
#annot= degerleri göster,linewidths=karelerin aralıklarını 0.5 yap
#fmt ondalık olarak goster yani 0.0 gibi goster 
plt.show()

    

    






