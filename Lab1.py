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
  
