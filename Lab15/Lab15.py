import sys
sys.path.append('lab15/build/lib.linux-x86_64-3.8')
import mod

#zad1
print('------------zad1-------------')
print(mod.met1(1,2))
print(mod.met1(1,2,5))
print(mod.met1(1,2,5,[2,3,4]))

#zad2
print('------------zad2-------------')
import random
import time

def InsertionSortPython(a):
  for i in range(1,len(a)):
    temp=a[i]
    j=i-1
    while j>=0 and temp<a[j]:
      a[j+1]=a[j]
      j-=1
    a[j+1]=temp
    
sizes=[10,10**2,10**3,10**4]
PythonTime=[]
CLangTime=[]
for s in sizes:
  tab1=[random.randint(0,s) for _ in range(s)]
  tab2=tab1[::]
  t1_start=time.time()
  InsertionSortPython(tab1)
  t1_end=time.time()
  PythonTime.append(t1_end-t1_start)
  t2_start=time.time()
  mod.met2(tab2)
  t2_end=time.time()
  CLangTime.append(t2_end-t2_start)

print(PythonTime)
print(CLangTime)

#zad3
print('------------zad3-------------')
d={1:5, 24:50, 17:34,100:200,555:333}
print(dict(mod.met3(d)))
