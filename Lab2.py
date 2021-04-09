#!/usr/bin/env python3
import keyword
import math

print( "Hello")
print(keyword.kwlist)

#dir wypisuje "funkcje" zawarte w bibliotece
#help wyświetla działanie danej "funkcji"
print(dir(math))
help(math.modf)

print(dir(''))
help(''.strip)

a=7
print(type(a))
b=3.7
print(type(b))
c=3,4
print(type(c))
print(c)
d,e=6, '3'
print(type(d))
print(type(e))
#a,b=b,a działa jako swap przy wcześniej zdefiniowanych a i b

f,*g=1,'2',3.,4,5
print(type(f))
print(type(g))
print(g)

#krotka - (el1,el2,el3,...)
#lista - [el1,el2,el3,...]

print(1/2, 1//2)
print(1./2,1.//2) 

print(2**3, pow(2,3), math.pow(2,3))
print(pow(2,3,4), pow(2,3,5))

print(math.ceil(1/3), math.floor(1/3), round(1/3), round(1/3,3))

print(math.modf(2.5))

print(min(1,2,3,4,5), max(1,2,3,4,5,6))

h=-1.7
i=-1
print(abs(h),math.fabs(h))
print(abs(i),math.fabs(i))

from math import sqrt
from cmath import sqrt as csqrt

k1=()
k2=(2)
k3=(2,)
print(type(k1),type(k2),type(k3))
A=float(input('A='))
B=float(input('B='))
C=float(input('C='))
Delta=B*B-4*A*C
if Delta>0:
  X1=(-B-sqrt(Delta))/(2*A)
  X2=(-B+sqrt(Delta))/(2*A)
  print(f'x1={X1:.3f},x2={X2:.3f}')
elif abs(Delta)<1e-6:
  X=-B/(2*A)
  print(f'x1=x2={X}')
else:
  X1=(-B-csqrt(Delta))/(2*A)
  X2=(-B+csqrt(Delta))/(2*A)
  print(f'x1={X1:.3f},x2={X2:.3f}')
##############################################################################

print('___________________LAB1____________________')

a=[]
b=[2,]
c=[1,2.3,'4',(5,6),[7,8]]
print(len(c))
print(c[0],c[-1])
#c[-2][1]=3 nie zadziała (krotka nie jest edytowalna)

list1=[1,3,5,7,6,4,2,0]
print(list1[:]) #cała lista
print(list1[2:5]) #od indeksu 2 do indeksu 4 (5 nie wchodzi)
print(list1[1:-3]) #od 1 do 3 od końca
print(list1[1:-2:2])#przedział ale co dwa
#############################
list2=c
list2[1]=[7,8,9]
print(list2,c)
print(id(list2),id(c))
############################
list3=c[:]
list3[1]=[8,9,10]
print(list3,c)
print(id(list3),id(c))

list3[-1][1]='7,8,9'
print(list3,c)
################################
list4=c.copy()
list4[1]=[9,10,11]
print(list4,c)
print(id(list4),id(c))
list4[-1][1]='8,9,9'
print(list3,c)

#import copy
#copy.copy() to samo co dwa poprzednie
#copy.deepcopy() tworzy prawdziwą kopię głęboką (listy wewnątrz nie są zmieniane w oryginale)

##################################
print(list1.index(2))
print(list1.count(2))

print(2 in list1,2 not in list1)

list1.insert(3,17) #wstawianie nowego elementu list na danym miejscu (17 na 3 miejscu)

list1.insert(-20,1) #wstawi na początku
list1.insert(20,1) #wstawi na końcu

print(list1)

#################################

list1[1:4]=[12,13,14,15]
print(list1)
list1[1:4]=[[12,13],]
print(list1)

list1.remove(7) #usuwa pierwsze wystąpienie wartości 3
print(list1)

del list1[4]
print(list1)

del list1[-3:]
print(list1)

print(list1.pop(-2))
########################################
list1.clear
print(list1)
#######################################
list1=[1]*10
list1[3]+=1
print(list1)
#####################################
l4=[[]]*10
l4[3].append(1)
print(l4)

l4=[[]for i in range(10)]
l4[3].append(1)
print(l4)

l4[3].append([1,2,3])
print(l4)
l4[3].extend([1,2,3])
print(l4)

###############################
l5=list(range(10)) 
print(l5)
l5=list(range(3,10)) #od 3 do 9
print(l5)
l5=list(range(2,11,2)) # od 2 do 10 co 2
print(l5)
l5=list(range(10,0,-1))
print(l5)

l5=[i for i in range(10)]
print(l5)
##################################3
for i in l5:
  i*=2
  print(i,end=', ')

for i,v in enumerate(l5):
  l5[i]=1 if v>0 else -1

print(l5)

########################
for i in l5:
  if i%2:
    break
else:
  print('kiedy?') #gdy pętla przejdzie nieprzerwana (nie będzie break'a)
########################
l6=[(l5[i],l5[-i-1]) for i in range(len(l5)//2)]
print(l6)
########################
l7=[(89,34),(92,31),(96,0),(48,30),(38,10)]
list7=l7[:]
list7.sort()
print(list7)

list7=l7[:]
list7.sort(key=lambda x: x[1])
print(list7)

list7=l7[:]
list7.sort(reverse=True)
print(list7)

list7=l7[:]
list7.reverse()
print(list7)
####ZAD2################
lz2=[2,3,4,5,4,3,2,3,4,5]
while lz2.index(2)+1>0:
  del lz2[lz2.index(2)]

print(lz2)

##########zad3############
lz3=[2,3,4,5,4,3,2,3,4,5]
for i in range(0,len(lz3),2):
  print(lz3[i])
##########zad4###########
for i in lz3[1::2]:
  print(i)
#########zad5############
for i in range(len(lz3)-1,0,-2):
  print(lz3[i])
#########zad6############
#########zad7############
lz7=[(i,lz3[i]) for i in range(len(lz3))]
print(lz7)
#########zad8############
lz7.sort(key=lambda x:x[1])
##########zad9############
lz9=[(i,lz3[i]) for i in range(len(lz3)) if not lz3[i]%2]
print(lz9)
###########zad10##########