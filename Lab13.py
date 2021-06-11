#zad1
print('------------zad1-------------')

import abc
import types
class Calka(abc.ABC):
  def __init__(self, start, end, N, Fun):
      if not isinstance(start, float) or not isinstance(start, float) or not isinstance(N, int) or not isinstance(Fun, types.FunctionType):
        raise TypeError
      
      self.start=start
      self.end= end
      self.n=N
      self.fun=Fun

  @abc.abstractmethod
  def integralVal(self):
    '''Metoda abstrakcyjna'''

class CalkaTrapez(Calka):
  def integralVal(self):
    self.step=(self.end-self.start)/self.n
    self.s = 0
    for i in range(self.n):
      self.s+=self.fun(self.start+(i*self.step))+self.fun(self.start+((i+1)*self.step))
    self.s*=(self.step/2)

    print("Wartosc calki metoda trapezow: ", self.s)

class CalkaSimpson(Calka):
  def integralVal(self):
    self.step=(self.end-self.start)/(2*self.n)
    self.s = self.fun(self.start)+self.fun(self.end)
    for i in range(1,2*self.n,2):
      self.s+=(4*self.fun(self.start+(i*self.step)))

    for i in range(2,2*self.n,2):
      self.s+=(2*self.fun(self.start+(i*self.step)))

    self.s*=(self.step/3)

    print("Wartosc calki metoda Simpsona: ", self.s)




fun=lambda x: x**2 + 4*x

z1_1=CalkaTrapez(0.0,4.0,4,fun)
z1_2=CalkaSimpson(0.0,4.0,4,fun)
#z1_BAD=CalkaTrapez("bad",4.0,4,fun)

z1_1.integralVal()
z1_2.integralVal()


#zad2
print('------------zad2-------------')
import random

class stos:
  def __init__(self, stos2=None):
    if type(stos2) is stos:
      self.vals=[el for el in stos2.vals]
    else:
      self.vals=[]
    
  def add(self, el):
    self.vals.append(el)

  def pop(self):
    return self.vals.pop(len(self.vals)-1)

  def add_stack(self, stos2):
    if type(stos2) is stos:
      for el in stos2.vals:
        self.add(el)
    
    else:
      print("Nie podano stosu!!!")

  def __len__(self):
    return len(self.vals)

  def __str__(self):
    OutStr=''
    for el in self.vals:
      OutStr+=str(el)+'\t'
    return OutStr
    

class sorted(stos):
  def __init__(self, stos2=None):
    if type(stos2) is stos:
      self.vals=[el for el in stos2.vals]
    else:
      self.vals=[]

  def add(self, el):
    if len(self.vals)==0 or el>=self.vals[-1]:
      self.vals.append(el)

  def add_stack(self,stos2):
    if type(stos2) is sorted:
      for el in stos2.vals:
        self.add(el)
    else:
      print("Stos nie jest posortowany!!!")


z2_1=stos()
z2_1.add(7)
z2_1.add(12)
z2_1.add(3)
print(z2_1)
popped=z2_1.pop()
print(z2_1)
print(popped)
print("Size of stack:", len(z2_1))

z2_2=stos(z2_1)
print(z2_1,'\t\t',z2_2)
z2_2.add(71)
z2_2.add(5)
print(z2_1,'\t\t',z2_2)
z2_2.add_stack(z2_1)
print(z2_1,'\t\t',z2_2)
print("Size of stack:", len(z2_2))

z2_3=sorted()
z2_3.add(7)
z2_3.add(12)
z2_3.add(3)
z2_3.add(25)
print(z2_3)
z2_3.add_stack(z2_1)
print(z2_3)
print("Size of stack:", len(z2_3))

z2_4=sorted(z2_1)
z2_4.add_stack(z2_3)
print(z2_4)
print("Size of stack:", len(z2_4))


sum=0
for _ in range(100):
  avg=sorted()
  for _ in range(100):
    avg.add(random.randint(0,100)) 
  sum+=len(avg)
print("Srednia dlugosc stosu posortowanego: ", sum/100)





#zad3
print('------------zad3-------------')
    
class MyWordCount:
  lines=0
  words=0
  chars=0
  def __init__(self,*files):
    self.files=[]
    for el in files:
      self.files.append(el)
    self.lines,self.words,self.chars=0,0,0
  
  def counter(self):
    for el in self.files:
      with open(el,"r") as file:
        self.lines,self.words,self.chars=0,0,0
        for line in file:
          self.lines+=1
          self.words+=len(line.split())
          self.chars+=len(line)
        MyWordCount.lines+=self.lines
        MyWordCount.words+=self.words
        MyWordCount.chars+=self.chars
        print(self.lines,'\t',self.words,'\t',self.chars,'\t',el)
    if len(self.files)>1:
      MyWordCount.countAll()

  @staticmethod
  def countAll():
    print(MyWordCount.lines,'\t',MyWordCount.words,'\t',MyWordCount.chars,'\t',"RAZEM")

z3=MyWordCount("testLab13_3.txt","test2Lab13_3.txt")
z3.counter()   
