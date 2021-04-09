import random
import sys
import string

while len(sys.argv)<2:
  print("Podaj jeden argument wywołania (string typu 'a+b*x-c')")
else:
  input1=sys.argv[1]
#zad1
print('------------zad1-------------')
def fun1(inpt):
  params=''
  params=''.join(i for i in inpt if i in string.ascii_lowercase)
  tr=str.maketrans(params, '0'*len(params))
  for i in tr:
    tr[i]=random.randint(48,57)
  tr[120]=120
  inpt=inpt.translate(tr)
  print(inpt)
  val=[random.random() for _ in range(10)]
  out=[(x,eval(inpt)) for x in val]
  return out

print(fun1(input1))

#zad2
print('------------zad2-------------')
def fun2(*inpt):
  out=[]
  i=inpt[0]
  for j in i:
    for k in inpt:
      if j not in k:
        break
    else:
        out.append(j)
  return out

print(fun2([1,2,3,5],(2,3,44,5),[2,3,5,6]))

#zad3
print('-----------zad3-------------')
def fun3(s1,s2,version=True):
  if version:
    out=[(s1[i],s2[i]) for i in range(min(len(s1),len(s2)))]
  else:
    out=[(s1[i],s2[i]) if i<min(len(s1),len(s2)) else (s1[i],None) if len(s1)>len(s2) else (None,s2[i]) for i in range(max(len(s1),len(s2)))]
  return out

print(fun3([1,2,4],(2,5,3,6,7),False))
print(fun3([1,2,4],(2,5,3,6,7)))

#zad4
print('-----------zad4-------------')
def fun4(inpt,nominal=(10,5,2)):
  out={}
  for i in nominal:
    if inpt>0:
      count=inpt//i
      inpt=inpt - count*i
      out.setdefault(i,count)
  if(inpt>0):
    return(f'Brak możliwości rozmienienia, pozostaje {inpt} reszty')
  else:
    return out

print(fun4(27))
print(fun4(28))
print(fun4(28,(5,2,1)))

#zad5
print('-----------zad5-------------')
def fun5(inpt,a,b,version='r'):
  count = 0
  found = False
  while (not found):
    if version=='r':
      rand=random.randint(a,b)
      found = True if rand==inpt else False
      a = rand+1 if rand<inpt else a
      b = rand-1 if rand>inpt else b
    else:
      rand=a+((b-a)//2)
      found = True if rand==inpt else False
      a = rand if rand<inpt else a
      b = rand if rand>inpt else b
    count=count+1
  return count

print("typ 'r':", fun5(4,0,20))
print("typ inny:", fun5(4,0,20,'o'))
