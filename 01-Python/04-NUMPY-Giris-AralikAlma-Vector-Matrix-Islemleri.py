# -*- coding: utf-8 -*-
#%%
#numpy kutuphanesi importing
import numpy as np
#1*15 lik vector
array1=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) 
print(array1.shape) #=> (15,0) 'lık bir vector
a=array1.reshape(3,5) # => 3x5 lik matrix yap
print(array1.ndim) # kaç boyutlu => 1
print(a.ndim) # 3x5 => 2 boyutlu 
print('data typeları :',array1.dtype.name)
#reshape yazmadan cok boyutlu array için=>
array2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#%%
#bu metod 0lardan 3x4 matris olusturur.
#append ile eklemek yerine bunu yapıp daha onceden
#yer ayırtırız.Append metodu beleği YORAR.
#*****parantez onemli asagıda np.zeros((3,4))
zeroMatrix=np.zeros((3,4))
zeroMatrix[2,1]=5 # Guncelleme olayi
zeroMatrix[0,0]=10 # (0,0)dan başlar.***
birliMatrix=np.ones((3,4))
bosMatrix=np.empty((3,4))
#--------
#1den başlayıp 40'a kadar 3er attırarak al ve dizi yap.
recursiveArange=np.arange(1,40,3)
#linspace esit aralıklı sayı getır
#1 ve 5 dahil olmak üzere 1-5 arasını 6 (5) eşit parcaya böl
a=np.linspace(1,2.5,3) # =>1,1.75,2.5
#=> 1 +49=50 tane sayıyı 25 eş parçaya böl.
b=np.linspace(1,49,25) 
#%% numpy basic operations=>
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2) #=> ** üzeri demek !!
# bir array için bir işlem yapmasını ıstedıgımızde
#her elemanı ıcın yapar. ve tek tek gosterır
print(np.sin(a))
print(a>2)
# Matrix carpimi (kuralları var 2x3 * 3x4)
import numpy as np
#matrix carpımları
c=np.array([[4],[6],[8]])
print(a*c) #=> BU ELEMAN ELEMAN CARPAR.
print(c*a)
#asıl matrix carpimi=>
print(a.dot(c)) #=> 4+12+24 =40
#%% TRANSPOSE ALMAK => 2x3 iken 3x2 yapmak
import numpy as np

d=np.array([[1,2,3],[4,5,6]])
print(d) #=> 2x3
print(d.T)#=> [[1,4],[2,5],[3,6]]   3x2 oldu

print(np.exp(d)) #=> d matrixinin exp'ini al

e=np.random.random((2,2))#=>2x2 random 0,1 arasında matrix
print(e)
print(e.sum())#=> tum degerlerı toplar
print(e.max())
print(e.min())
print(e)
print('--col col ,row row toplama---')
#satır satır yada stun stun toplamak ıstersek=>
print(e.sum(axis=0)) #"col col toplar "+
print(e.sum(axis=1)) #"row row toplar "+
np.sqrt(e) #=>e nin karakokunu aldık
np.square(e) #=> e nin karesini aldık
#%% Indexin and slicing
import numpy as np
a1=np.array([1,2,3,4,5,6,7])#=> bu bir vector.
print(a1[0:3])
reverseArray=a1[::-1] #=> TERS CEVIRME***
print(reverseArray) #=> [7,6,5,4,3,2,1]

a2=np.array([[1,2,3],[5,4,8],[4,2,9]])
reverseA2=a2[::-1]
#print(reverseA2); #=> [[4,2,9],[5,4,8],[1,2,3]]

print('----')
print(a2)
print(a2[1,:]) #=> 1. row u al komple al !!
print(a2[:,2]) #=> 2.columu al komple.!!
print(a2[2,1]) #=> bu nokta atışı.
print(a2[-3,-3]) #=> r,c için geriden başlayarak say

#a2 arrayi için 4 8 ve 2 9 olan 2x2 sag alttakı kareyı alalım
print(a2[1:3,1:3])
#ortadaki 4 2 yi alalım asagı dogru gıden
print(a2[1:3,1:2])

#enson satırı alalım
print(a2[-1,:])
#%% shape manipulation Boyut değiştirme 
# 3x3 ten 9x0 a mesela
import numpy as np
m1=np.array([[1,2,3],[4,5,6],[7,8,9]])
v1=m1.ravel()#=> ONEMLII ** matrixten vectore cevırme
m2=v1.reshape((3,3))#=> vectordan matrixe
m3=m2.T #=> matrix2 nin Transposunu alalım

#resize((2,3)) metodu onemlı dırek kullanıldıgı 
#matrixi değiştirir.
m4=np.array([[2,3],[5,6],[8,1]])
#m4.resize(2,3) dersek 2x3 olacak ve boyle kalacak
#m4.reshape(2,3) te 2x3 e değiştirir. ama getlemek lazım başka matrix üzerine
#%% Arraylerin birleştirilmesi stacking arrays
import numpy as np

ar1=np.array([[1,2],[4,7]])
ar2=np.array([[-1,-2],[-4,-7]])
#dikey ve yatay birleştirme yapabıliriz.
#vertical:dikey , hori:yatay
print(ar1)
print(ar2)
print('vstack birleştirme asagıda')
ar3=np.vstack((ar1,ar2))
print(ar3)
print('hstack asagıda')
ar4=np.hstack((ar1,ar2))
print(ar4)

#%% List to array , arry to list**ONEMLI
# Convert and Copy
import numpy as np
#list to array
l1=[1,2,3,4]
aa1=np.array(l1)
#array to list
l2=list(aa1)

#COPY 
aa2=aa1.copy() #=> yeni alan olusturur.
# direk aa2=aa1 deme . Memoryde bir tane 
#olusturuyor. yani aa2 değiştiginde aa1 de 
#degisir copy yapmazsan.






