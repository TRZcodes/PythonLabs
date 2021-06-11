#zad1
print('------------zad1-------------')

from random import choices as los
from matplotlib import pyplot as plt

class IFS:
  def __init__(self,params,weights=None):
    self.x=0 
    self.y=0
    self.xTab=[]
    self.yTab=[]
    self.parTab=params
    self.weTab=weights
  
  def xyChange(self, it_num):
    for _ in range(it_num):
      par=los(self.parTab,weights=self.weTab,k=1)
      par=par[0]
      self.x=par[0]*self.x+par[1]*self.y+par[2]
      self.y=par[3]*self.x+par[4]*self.y+par[5]
      self.xTab.append(self.x)
      self.yTab.append(self.y)
  
  def prnt(self):
    plt.scatter(self.xTab,self.yTab,0.1,"blue",'.')
    plt.show()

'''
ifs1=IFS(((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236), (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)), (0.90, 0.05, 0.05))
ifs1.xyChange(100000)
ifs1.prnt()'''
'''ifs2=IFS(((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513), (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43), (0.119, 0, -2.555, 0, 0.053, 4.536), (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235), (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569), (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113), (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43), (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487), (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716), (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298), (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487)))
ifs2.xyChange(100000)
ifs2.prnt()'''

'''
ifs3=IFS(((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)),  (0.8, 0.2))
ifs3.xyChange(100000)
ifs.prnt()'''

#zad2
print('------------zad2-------------')

from math import sqrt

class Wektor:
  def __init__(self,params=[]):
    self.parTab=[]
    for i in params:
      self.add(i)
  
  def __len__(self):
    return len(self.parTab)

  def __add__(self,otherV):
    if type(otherV) is Wektor:
      if len(self) == len(otherV):
        out=Wektor()
        for i in range(len(self)):
          out.add(self.parTab[i]+otherV.parTab[i])
        return out
  
  def __sub__(self,otherV):
    if type(otherV) is Wektor:
      if len(self) == len(otherV):
        out=Wektor()
        for i in range(len(self)):
          out.add(self.parTab[i]-otherV.parTab[i])
        return out
  
  def __mul__(self,num):
    out=Wektor()
    for i in range(len(self)):
      out.add(self.parTab[i]*num)
    return out

  __rmul__=__mul__

  def Vlen(self):
    return sqrt(sum(i**2 for i in self.parTab))

  def add(self,num):
    self.parTab.append(num)

  def scalMult(self, otherV):
    out=0
    if type(otherV) is Wektor:
      if len(self) == len(otherV):
        for i in range(len(self)):
          out+=self.parTab[i]*otherV.parTab[i]
        return out

  def vecMult(self,otherV):
    out=Wektor()
    lenT=len(self)
    if type(otherV) is Wektor:
      if lenT == len(otherV):
        for i in range(lenT):
          out.add((self.parTab[(i+1)%lenT]*otherV.parTab[(i+2)%lenT])-(self.parTab[(i-1)%lenT]*otherV.parTab[(i-2)%lenT]))
        return out

  def mixMult(self,v1,v2):
    if type(v1) is Wektor and type(v2) is Wektor:
      if len(self) == len(v1) and len(self)==len(v2):
        return self.scalMult(v1.vecMult(v2))
  
  def __str__(self):
    outStr="("
    for i in range(len(self)):
      outStr+=str(self.parTab[i])
      if i!=len(self)-1:
        outStr+=','
    outStr+=')'
    return outStr

v1=Wektor([1,1,1])
v2=Wektor([2,3,4])
v3=Wektor([2,2,4])
print(v1+v2)
print(v1-v2)
print(v2*3)
print(3*v2)
print(v1.scalMult(v2))
print(v1.vecMult(v2))
print(v2.vecMult(v3))
print(v1.mixMult(v2,v3))


#zad3
print('------------zad3-------------')

def fun1(v1,v2):
  return v1.scalMult(v2)

def fun2(q,v1,v2,v3):
  return q*(v1+v2.vecMult(v3))

def fun3(q,v1,v2):
  return q*v1.scalMult(v2)
