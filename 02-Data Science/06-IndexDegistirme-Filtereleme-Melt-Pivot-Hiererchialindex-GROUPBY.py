# -*- coding: utf-8 -*-
#%%
import pandas as pd
pokeData=pd.read_csv('pokemon.csv')

pokeData=pokeData.set_index('#') #=>idye göre index yap
#Artık 0 indexli deger yok dikkat ettıysen
pokeData['HP'][1] #=> 45 yani öncekinin 0. indexlisinin degeri

#=> loc ' tekrar donelim
pokeData.loc[[2,3],'Type 1':'HP'] 
#=> 2ve3. rowu al Type 1 ile HP arasındaki colları al
#loc= location demek
# nokta atısı yapacaksan [] yaz  ve araya vırgul koy
# aralık alacaksan = [] YOK, ve araya : koy
pokeData.loc[:,['HP']] #=> rowlardan hepsini ,coldan sadece HP
pokeData.iloc[0,3]

# iki col secmek
ilk5=pokeData.head()
ilk5[['HP']] #=> BU BIR DATAFRAME (col namesı felan var zaten)
ilk5['HP'] #=> BU BIR SERI 

print(ilk5[['HP','Attack']]) #=> IKI COL ALDIK YENI SAMPLE OLUSTU

#%%
#SLICING DATA (Aralık secmeye yarar)
terstenSirali=ilk5[::-1]
pokeData.loc[1:10,"Speed":]#=>1-10 row,;Speed -Sonakadar col

#FILTERING DATA
can100Filtresi=pokeData.HP>100
cani100denbuyukOlanlar=pokeData[can100Filtresi]
legendaryTrueOlanlar=pokeData[pokeData['Legendary']==True]
pokeData.Legendary.value_counts() #=> Legendarynin degerlerine göre sayısı

#Combining Filters
atak100Filtresi=pokeData.Attack>100
atak100can100olanlar=pokeData[can100Filtresi & atak100Filtresi]

#Legendary=True ve Type 1'i Psychic olanlar
legendaryTrue=pokeData["Legendary"]==True
psychicfiltre=pokeData['Type 1']=='Psychic'
OdedigindenOlanlar=pokeData[legendaryTrue & psychicfiltre]

# @@ONEMLI HIZI 20DEN KUCUK OLANLARIN HPLERINI VE NAMELERINI GETIR @qqqqqqqq
yeni1=pokeData[["HP","Name"]][pokeData.Speed<20]

#--------------------------------------------

#DATA DEGISIMI ICIN METOD OLUSTURMAK VE APPLY METODU

#apply metodu ıle belırledıgımız datayi etkileyebılırz
#mesela butun pokemonların hızlarını 2ye bolcem
def ikiyeBol(deger):
    return deger/2

pokeData.Speed.apply(ikiyeBol)

#Metod olmadanda lambda func ile yapabılırz
pokeData.Speed.apply(lambda n:n/2)

pokeData['yeni-col']=pokeData.Attack+pokeData.Defense

#%% INDEX OBJECTS ANDA LABELED DATA
#-datamın indexi hangi col?
print(pokeData.index.name)
#degistirelim index nameyi
pokeData.index.name="ind"
print(pokeData.index.name)
#indexi verme aralıgını degıstırelbılırım.0 ,1 den baslamasın
#100 den baslasın-900e kadar ,1er 1 er art
pokeData.index=range(100,900,1)
pokeData.head()
#indexi baska feature yapma=>
#pokeData.index=pokeData['Attack'] BU DEGIL ASAGIDA
"""
ASAGISI ONEMLI
"""
#%% HIERARCHICAL INDEXING ***
import pandas as pd 
pokData=pd.read_csv('pokemon.csv')
#iki indexli olabilir
ikiindexli=pokData=pokData.set_index(['Type 1','Type 2'])

#%%
#PIVOTING DATA FRAMES
dic1={"treatment":['A','A','B','B'],"gender":['F','M','F','M'],
      'age':[15,24,55,11],'response':[14,55,22,44]}
data1=pd.DataFrame(dic1)

data2=data1.pivot(index="treatment",columns='gender',values='response')
#PIVOT ILE Indexi Treatmnet yaptık collara gender'ı verdık ve degerler ıcınde response aldık

# MELTING DATA FRAMES

melteddata=pd.melt(data1,id_vars='treatment',value_vars=['age','response'])
#treatmen sabit kalsın variable olarak age ve response al ve valuelerını yaz.

#GROUP BY METODU ***************************
data1.groupby('treatment').mean()
#treatmentna gore grupla ve degerlerın ort bul
data1.groupby('treatment').age.max()
#threatment'ı A olanlar ıcın max yas
#threatment'ı B olanlar ıcın max yas

data1.groupby('treatment')[['age','response']].min()

