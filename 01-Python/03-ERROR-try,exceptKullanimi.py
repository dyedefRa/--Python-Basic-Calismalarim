# -*- coding: utf-8 -*-
#%% sytax error
#Once syntax hatalarını gosterır sonrasında exp hatatları
#gosterır.
print(9)
#print 9
int(10.0)
#int 10

#%% exceptions hatalari

a=10
b="2"
liste=[1,2,3]
print(sum(liste))

print(str(a)+b)
#%% TRY CATCH
try:
    a=10/0
except ZeroDivisionError:
    a=0
