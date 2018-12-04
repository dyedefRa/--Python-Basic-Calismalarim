# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 00:15:05 2018

@author: Baki
"""
#%% mathplotlib => gorselleştirme kutp.
#line plot,scotter plot,bar plot,subpilots,histogram
import pandas as pd
df=pd.read_csv("iris.csv")
print(df.columns)#=> featureleri neler?
#=> Species' featuresinde kaç farklı veri var
print(df.Species.unique())
print(df.info())
print(df.describe())
#--------------
#=>coldan species leri 'Iris-setosa' olanları getir
setosalar=df[df["Species"]=="Iris-setosa"]
versicolorlar=df[df.Species=="Iris-versicolor"]
virginicalar=df[df.Species=="Iris-virginica"]
print('---Karsilastırma----')
#Türleri tek tek alalım
print(setosalar.describe())
print(versicolorlar.describe())
print(virginicalar.describe())
#%% GORSELLESTIRME BASLANGICI
import matplotlib.pyplot as plt

# => Id col unu silelim
dataFrame1=df.drop(["Id"],axis=1)
dataFrame1.plot(grid=True,linestyle=":",alpha=0.8) 
#=> keskin geçişler tür değişimiyle alakalıdır
#linestyle: çizgiler yerine ne olsun,alpha= opacity
#Her turun her col ıle grafıgı gozukuyor
plt.show()

#%% Cinse baglı olarak her bir cins için (yukarı bu cınslerı aldık)
#id-PetalLengthCm grafigi cizdireceğiz.
plt.plot(setosalar.Id,setosalar.PetalLengthCm,color="red",label="Setosa")
plt.plot(versicolorlar.Id,versicolorlar.PetalLengthCm,color="blue",label="Versicolor")
plt.plot(virginicalar.Id,virginicalar.PetalLengthCm,color="green",label="Virgin")
plt.plot()
plt.legend()#=> labeli gosteriyor yani grafik adını
plt.xlabel("Id (x)")
plt.ylabel("Petal Length Cm")
plt.show()

#%% SCATTER PLOTTT
plt.scatter(setosalar.PetalLengthCm,setosalar.PetalWidthCm,color="red",label="Setosa")
plt.scatter(versicolorlar.PetalLengthCm,versicolorlar.PetalWidthCm,color="blue",label="Versicolor")

plt.scatter(virginicalar.PetalLengthCm,virginicalar.PetalWidthCm,color="green",label="Virgin")
plt()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.legend()
plt.title("PetalLength-PetalWidth CM")
plt.show()
#%% HISTOGRAM PLOT 
#=>setosa türünde SepalLengthCm col unun sayısına gore grafigi
plt.hist(setosalar.SepalLengthCm,color="red",bins=20)
# bins=20> x i 20ye bol
plt.xlabel("SepalLengthCm")
plt.ylabel("Adet")
plt.show()
#%% BAR PLOT
#numpy kullanalım bundada
import numpy as np
x=np.array([1,2,3,4,5,6,7])
y=x*2+5
plt.bar(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Nerelerde kullanırız? - bu ornek olmadı :(
#-Ülkelerin gelir dagılımı
#liste=["Turkey","ABD","Almanya","Fransa","Holland","Pakistan","Iran"]
#
#plt.bar(liste,x)
#plt.show()
#%% SUB PLOTS 
#=> COLLARA GORE AYIRIP CIZIYOR.
#Ayrı ayrı cızdırmeye yarıyor
dataFrame1.plot(grid=True,linestyle=":",alpha=0.8,subplots=True) 
setosalar.plot(grid=True,subplots=True)

#%% (3,3,9) demek 3 row 3 col lu sayıda grafık ve 9.grfıgı verıyorum demek
plt.subplot(3,3,9)
plt.plot(setosalar.Id,setosalar.PetalLengthCm,color="red",label="Setosa")
plt.ylabel("Setosa")
plt.subplot(3,3,1)
plt.plot(versicolorlar.Id,versicolorlar.PetalLengthCm,color="blue",label="Versicolor")
plt.ylabel("Versicolor")
plt.show()














