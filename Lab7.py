#zad1
print('------------zad1-------------')

def gen1_1():
  n=0
  while True:
    yield n
    n+=1

def gen1_2(seq):
  for i in seq:
    if i==sum((j for j in range(2,i) if not i%j),1):
      yield i

def gen1_3(seq,x):
  for i in seq:
    if i>x:
      break
    yield i

for i in gen1_3(gen1_2(gen1_1()),10000):
  print(i)

#zad2
print('------------zad2-------------')
from math import log

def gen2():
  u=0.
  x0=1.
  a=0.05
  i=1
  x=1.
  while x<=1.5:
    yield x,u,log(x)
    u+=a/x
    x=x0+i*a
    i+=1

for i in gen2():
  print (i)

#zad3
print('------------zad3-------------')
def gen3(n):
  current=n
  a=[]
  for i in range(n-1,0,-1):
    current=n
    a=[]
    while i>0:
      while current>0 and current>=i:
        a.append(i)
        current-=i
      i=current  
    yield a

for i in gen3(4):
  print(i)


#zad4
print('------------zad4-------------')
import random

def gen4():
  last=-1
  current=random.random()
  while current>0.1:
    if abs(last-current)>0.4:
      yield current
      last=current
    current=random.random()

for i in gen4():
  print(i)

#zad5
print('------------zad5-------------')
def myRange(start,stop=None,step=1.0):
  start=float(start)
  if stop is None:
    start,stop=0.,start
  while True:
    if step>0 and start>=stop:
      break
    if step<0 and start<=stop:
      break
    if step==0:
      break
    yield start
    start+=step

rangeTest=(range(8), range(-8), range(1,8), range(8,1), range(1,8,2), range(1,8,-2), range(8,1,2), range(8,1,-2))
myRangeTest=(myRange(8), myRange(-8), myRange(1,8), myRange(8,1), myRange(1,8,2), myRange(1,8,-2), myRange(8,1,2), myRange(8,1,-2))

for i in range(8):
  print("\nrange:",end=' ' )
  for j in rangeTest[i]: 
    print(j,end=' ')
  print("\nmyRange:",end=' ')
  for k in myRangeTest[i]: 
    print(k,end=' ')
