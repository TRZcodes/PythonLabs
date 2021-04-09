#!/usr/bin/env python3

import random
import sys
import copy
import string

if len(sys.argv)<2:
  print("Podaj jeden argument wywołania (liczba naturalna)")
else:
  k=int(sys.argv[1])

#zad1

l1=[random.randint(0,5*k) for i in range(k)]

l1org=copy.deepcopy(l1)

dict1=dict((i,0) for i in l1)
for i in range(100):
  random.shuffle(l1)
  for j in range(k):
    if l1[j] is l1org[j]:
      dict1[l1org[j]]+=1
#print(dict1)

#zad2
str1=''

str1+='.'.join(random.choice(string.ascii_lowercase) for i in range(k))
#print(str1)

#zad3

l3=[random.randrange(0,20) for i in range(100)]
dict2={}

for i,j in enumerate(l3):
  dict2.setdefault(j,[]).append(i)
#print(dict2)

#zad4
def isPal(x):
  xstr=str(x)
  if xstr==xstr[len(xstr)-1::-1]:
    return True
  else:
    return False
  


dict3=dict((random.randint(10,100),False) for i in range(1000))
for j in dict3:
  if isPal(j):
    dict3[j]=True

#print(dict3)

#zad5
dict4=dict((i,random.randrange(1,100)) for i in range(1,11))
dict5=dict((i,random.randrange(1,100)) for i in range(1,11))


dict4=dict((dict4[i],i) for i in range(1,11))
dict5=dict((dict5[i],i) for i in range(1,11))

dict6=dict((i,(dict4[i],dict5[i])) for i in dict4 if i in dict5)

#print(dict4, dict5, dict6)