#zad1
print('------------zad1-------------')

class FiboOneClass:
  def __init__(self,maxi):
    self.maxi=maxi
    self.first=0
    self.second=1
  
  def __iter__(self):
    return self

  def __next__(self):
    elem=self.first
    if elem>self.maxi:
      raise StopIteration
    self.first,self.second=self.second, self.first+self.second
    return elem

class FiboTwoClasses:
  def __init__(self,maxi):
    self.maxi=maxi
    self.first=0
    self.second=1

  def __iter__(self):
    return FiboTwoClasses(self.maxi)
  
  def __next__(self):
    elem=self.first
    if elem>self.maxi:
      raise StopIteration
    self.first,self.second=self.second, self.first+self.second
    return elem

print("--Jedna klasa--")

test1=FiboOneClass(100)
for _ in range(4):
  for i in test1:
    print(i, end=' ')
  print()

print("--Dwie klasy--")

test2=FiboTwoClasses(100)
for _ in range(4):
  for i in test2:
    print(i, end=' ')
  print()

#przy użyciu jednej klasy jesteśmy w stanie tylko raz przejść przez obiekt, tworząc dwie możemy zrobić to wielokrotnie


#zad2
print('------------zad2-------------')

import random

class PseudoIter:
  def __init__(self,m,a,c,x0):
    self.m=m
    self.a=a
    self.c=c
    self.x=x0

  def __iter__(self):
    return self

  def __next__(self):
    self.x=(self.a*self.x+self.c)%self.m
    return self.x/self.m

pseudo=PseudoIter((2**31)-1,7**5,0,1)

myList=[0 for _ in range(10)]
randList=[0 for _ in range(10)]

for _ in range(10**5):
  myPoint=(next(pseudo),next(pseudo))
  randPoint=(random.random(),random.random())
  for i in range(1,11):
    myList[i-1]+=(myPoint[0]<=0.1*i and myPoint[1]<=0.1*i)
    randList[i-1]+=(randPoint[0]<=0.1*i and randPoint[1]<=0.1*i)

for i in range(10):
  myList[i]=(myList[i]/10**5)*100
  randList[i]=(randList[i]/10**5)*100

print('--Procent punktów w kwadratach dla iteratora--')
print(myList)
print('--Procent punktów w kwadratach dla random.random()--')
print(randList)

#zad3
print('------------zad3-------------')

import scipy.misc
import math


class zeroIter:
  def __init__(self,fun,x,eps):
    self.fun=fun
    self.x=x
    self.eps=eps
  
  def __iter__(self):
    return self

  def __next__(self):
    prevX=self.x
    self.x=self.x-self.fun(self.x)/scipy.misc.derivative(self.fun,self.x)
    if abs(self.x-prevX)<self.eps:
      raise StopIteration
    return self.x

f=lambda x: math.sin(x)-(0.5*x)**2
test3=zeroIter(f,1.5,10**-5)

for i in test3:
  print(i)
