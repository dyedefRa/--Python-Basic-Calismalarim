#%% While 
i=0
while(i<5):
    print(i)
    i=i+1
#%% for ile (index,value) degeri almak
    
liste=[11,22,33,44]
for i,v in enumerate(liste):
    print(f'{i} indexli deger= {v}')
#%% Dictionary ile (key,value) almak
    
sozluk={34:'Istanbul',35:'Izmır',77:'Yalova',46:'Kahraman Maras'}
for key,value in sozluk.items():
    print(f'{key} keyin degeri = {value}')
#%% DataFrameden (index,value) almak
    
import pandas as pd 
pokeData=pd.read_csv('pokemon.csv')
#=> [0:1] ilk elemanını al , [0:2] , 0 ,1 indexli elemanı al.
for i,v in pokeData[['Attack']][0:1].iterrows():
    print(f'Index:{i} || Value:{v}')
    
#%% Dictionary listeden daha hızlı @@@@@@@@@@@@@@@@@
    
sozluk={'Istanbul':34,'Izmir':35,'Yalova':77}
sozluk.keys()
sozluk.values()
#yeni entry eklemek için
sozluk['Maras']=46
#silmek için
del sozluk['Maras']
#------------
#dictionarym de key ismi varmı yokmu diye sormak için=>T/F
'Izmir' in sozluk
#dictionary i boşaltamak için =>
#sozluk.clear()
#Silmek için=>
#del sozluk
#%% PANDAS
#CSV Importu için=>
import pandas as pd
dataFrame1=pd.read_csv('pokemon.csv')#=> dataFrame
#Pandasta Seriler ve DataFrame olmak uzere iki çeşit veri var
seri1=dataFrame1['Defense'] #=> bu bir seri
dataFrame2=dataFrame1[['Defense']] #=> bu da bir DataFrame!