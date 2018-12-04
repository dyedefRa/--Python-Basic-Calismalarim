# -*- coding: utf-8 -*-
#%%User Defined Function
"""Bunun adı docstringtir.Fonksiyon vsde acıklama yapmaya yarar"""

def tuple_fonk():
    """ Bu fonk tuple donderir"""
    t = (1,2,3)
    return t

a,b,_=tuple_fonk()
#=> Tuple olusturabılıriz.Bazı fonklarda birden fazla deger
#doner.İşimize yaramayan degır ıcın _ demek yeterli.
#%%Scope ne demek?
#-Global,Local ve Built in scope cesitleri vardır
x=2 #=> bu GLOBAL SCOPE
def f():
    x=3#=> burası LOCAL SCOPE
    return x
print(x)
print(f())
#-----------
a=5
def g():
    b=2*a#=> LOCALde a tanımlımı? yoksa globaldde ara
    return b
#%%
#OZET Once LOCAL scope'a bakılıyor.Yoksa GLOBAL'e bakılıyor.
#Oda yoksa Builtings scope'a bakılır
#Daha önceden atanmış deger varmı 
#    Builtinslere bakmak için=>
    import builtins
    dir(builtins)
#%% Nested Function-DEFAULT & FLEXIBLE ARGUMENTS
#Nested Function:Icice fonk.


#Default Arguments
def f1(a,b=1,c=2):
    return a+b+c#=>b ve c için default deger verdık
print(f1(5,c=3))#=>5+1+3=9


#FLEXIBLE Arguments=Parametre => *args
def etiketEkle(*args):
    donecek=""
    for x in args:
        donecek=donecek+' '+x
    return donecek
#=> YANI PARAMS . Kaç parametre alıncak bılınmıyorsa
#*args kullanılır argument(parametre) olarak
    
#DICTIONARY PARAMETRE VERMEK ICIN => **kwargs
#parametreye dict degerleri atman gerek ise kullanırsın
#ve kaç tane verecegegını bılmıyorsan => **kwargs

def forDict(**kwargs):
    for key,value in kwargs.items():
        print(f'KEY={key} | VALUE={value}')

forDict(Selam=True,safasf='asfsaf')
#%% LAMBDA FUNCTION
#fonk yazmanın kısa yolu

kareAl=lambda x:x**2
print(kareAl(4))

#%% ANONYMOUS FUNCTION
#Isimsiz fonk.Map ederiz bir deger listesini bir fonksuonya.
number_list=[1,2,3]
y=map(lambda x:x**2,number_list)
print(list(y))

#%% ZIP METODU ( birleştir)
list1=[0,2,3]
list2=["ali","hakan","murat"]
#Bu listeleri birleştirecegim ve ilk verdıgım list1 yeni listenin
#indexi olacak 2. ise degerleri olacak
yeni_objem=zip(list1,list2)
print(yeni_objem)
#bu sekılde list olmuyor. Bu obje oluyor
yeni_list=list(yeni_objem)
#%% Condition And Iterable ******ONEMLI***LIST COMPREHENSION
""" BURSAI ONEMLI IF-ELSE-IF-ELSE OLAYI (DOUBLE) """
#iterable olayı=>
number1=[5,10,15]
number2=[sayi+1 if sayi==10 else sayi+5 if sayi<7 else sayi-3 for sayi in number1]
number3=[3*x+5 if x<7 else int(x+(x/3)) if x>11 else 2*x for x in number1]
#=> Eger sayi 7den kucuk ıse 3*x+5 olsun degılse => x>11 mi diye bakıcaz. evet ise (x+x/3) olsun degıl ıse 2*x olsun..
#Yani ilk elseden sonra ki ifın arasındaki deger için x>11 durumundakilere gırıyor. degıl ıse 2*x
kelimeList=['a','b','c']
kelimeList2=[kelime+'li' if kelime=='a' else kelime+'aki' if kelime!='c' else kelime+'eyhan' for kelime in kelimeList]   

#PANDAS ORNEGI
import pandas as pd
pokeData=pd.read_csv('pokemon.csv')

ortalamaHizlari=sum(pokeData.Speed)/len(pokeData.Speed)
ortalamaHizlari=int(ortalamaHizlari)
pokeData['HizFeature']=['Ortalama' if hiz==ortalamaHizlari else 'Hızlı' if hiz>ortalamaHizlari else 'Yavaş' for hiz in pokeData.Speed]
    
    
    
    
    
    
    
    

    