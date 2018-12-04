#%%

#dizi={'2',2,'saf'}
liste=[1,2,14,3,11]
sonuncuyual=liste[-1]
# 1 2. indexli elemanı  al dedik.
indexegoretoplual=liste[1:3]

#listenin kendine özgü fonksiyonları için=>
#dir(list)
#oradaki metodlarının ne işe yaradıgnı ogrenemk için=> Bunları console yaz.
#help(list.extend)

#list.pop() index numarasına gore sıler ve sıldıgın valueyı doner
#%% TUPLE ()=> bu sekılde tanımlarsın
t=(1,23,42,1,4,2)
#t.count(3) bu metod t icinde kactane 3
#degerının oldugunu soyler
#%% DICTIONARY

sozluk={'ali':20,'veli':25,'osman':40}
#'clear','copy','get','items', 'keys','pop''values'

#%%IF 
#if((10>2 or False!=True)and 1==1):
var1=10
var2=10
if(var1>var2):
    print('ilki buyuk')
elif(var1==var2):
    print('Aynı')
else:
    print('ikinci buyuk')

listem=[1,2,3,4,5]
#6 degerı bu lıstede varmı?
#**************************ONEMLII***************€€€€€€€
deger=6
if deger in listem:
    print(f'Evet {deger} sayisi listede')
else:
    print(f'Hayır {deger} sayisi listede degil')

#%% QUIZ YUZYIL BUL
def yuzyilbul(deger):
    if deger<100:
        donecek=1
    elif(deger>2005):
         return 'YOK'
    else:
        donecek=int(deger/100)+1
    return f'{deger} yılı : {donecek}. yuzyıldır'
#%%for loop
#for x in range(1,11):
#    print(x)
#    
#for s in 'selamlar as':
#    print(s)
#for a in 'savas'.split('v'):
#    print(a)

liste=[1,5,4,2,5,1,6,2,]
deger=0
for sayi in liste:
    deger+=sayi
print(deger)
print(sum(liste))
#%% while loop
deger=True
i=0
while(deger):
    i=i+1
    if i==5:
        deger=False
    print(i)
#%% son QUIZ
listee=[15,26,35,15,63,61,7,215]
def enkucuguBul(listem):
    enkucuk=max(listee)
    for sayi in listem:
        if sayi<enkucuk:
            enkucuk=sayi
            
    return enkucuk


