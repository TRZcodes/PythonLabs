#zad1
print('------------zad1-------------')

class Point:
  def __init__(self):
    self.x=0
    self.y=0

@property
def x(self):
  return self._x

@property
def y(self):
  return self._y

@x.setter
def x(self, val):
  self._x=val

@y.setter
def y(self, val):
  self._y=val

@x.getter
def x(self):
  return self._x

@y.getter
def y(self):
  return self._y

z1_1=Point()
print("pkt1=",z1_1.x,z1_1.y)
z1_1.x=5
z1_1.y=4
print("pkt1=",z1_1.x,z1_1.y)

#zad2
print('------------zad2-------------')

def PointRange(begin, end):
  def fz(fun):
    def fw(pkt1,pkt2):
      if all((begin<=pkt1.x<=end,begin<=pkt1.y<=end,begin<=pkt2.x<=end,begin<=pkt2.y<=end)):
        return fun(pkt1,pkt2)
      else:
        raise ValueError
    return fw
  return fz

@PointRange(-5,5)
def Add(pkt1,pkt2):
  if type(pkt1) == Point and type(pkt2) == Point:
    out = Point()
    out.x=pkt1.x+pkt2.x
    out.y=pkt1.y+pkt2.y
    return out

@PointRange(-5,5)
def Sub(pkt1,pkt2):
  if type(pkt1) == Point and type(pkt2) == Point:
    out = Point()
    out.x=pkt1.x-pkt2.x
    out.y=pkt1.y-pkt2.y
    return out

z2_1=Point()
z2_1.x=-2
z2_1.y=-4

z2_BAD=Point()
z2_BAD.x=2
z2_BAD.y=7

print("pkt2=",z2_1.x,z2_1.y)
print(z2_BAD.x,z2_BAD.y)

add12=Add(z1_1,z2_1)
print("pkt1+pkt2=",add12.x,add12.y)

sub12=Sub(z1_1,z2_1)
print("pkt1-pkt2=",sub12.x,sub12.y)

#addBad=Add(z1_1,z2_BAD)
#subBad=Sub(z1_1,z2_BAD)

#zad3
print('------------zad3-------------')
import math

class Shapes:
  def __init__(self):
    pass

  @staticmethod
  def TriCirc(p1,p2,p3):
    if all((type(p1) == Point, type(p2) == Point, type(p3) == Point)):
      a=math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
      b=math.sqrt((p3.x-p2.x)**2+(p3.y-p2.y)**2)
      c=math.sqrt((p1.x-p3.x)**2+(p1.y-p3.y)**2)
      return a+b+c
    else:
      raise TypeError

  @staticmethod
  def TriArea(p1,p2,p3):
    if all((type(p1) == Point, type(p2) == Point, type(p3) == Point)):
      a=math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
      b=math.sqrt((p3.x-p2.x)**2+(p3.y-p2.y)**2)
      c=math.sqrt((p1.x-p3.x)**2+(p1.y-p3.y)**2)
      p=(a+b+c)/2
      return math.sqrt(p*(p-a)*(p-b)*(p-c))
    else:
      raise TypeError

  @staticmethod
  def QuadCirc(p1,p2,p3,p4):
    if all((type(p1) == Point, type(p2) == Point, type(p3) == Point, type(p4) == Point)):
      a=math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
      b=math.sqrt((p3.x-p2.x)**2+(p3.y-p2.y)**2)
      c=math.sqrt((p4.x-p3.x)**2+(p4.y-p3.y)**2)
      d=math.sqrt((p1.x-p4.x)**2+(p1.y-p4.y)**2)
      return a+b+c+d
    else:
      raise TypeError

  @staticmethod
  def QuadArea(p1,p2,p3,p4):
    if all((type(p1) == Point, type(p2) == Point, type(p3) == Point, type(p4) == Point)):
      a=math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
      b=math.sqrt((p3.x-p2.x)**2+(p3.y-p2.y)**2)
      c=math.sqrt((p4.x-p3.x)**2+(p4.y-p3.y)**2)
      d=math.sqrt((p1.x-p4.x)**2+(p1.y-p4.y)**2)
      p=(a+b+c+d)/2
      return math.sqrt((p-a)*(p-b)*(p-c)*(p-d))
    else:
      raise TypeError


z3_1=Point()
z3_1.x=0
z3_1.y=0

z3_2=Point()
z3_2.x=0
z3_2.y=8

z3_3=Point()
z3_3.x=6
z3_3.y=0

z3_4=Point()
z3_4.x=6
z3_4.y=8

print(Shapes.TriCirc(z3_1,z3_2,z3_3))
print(Shapes.TriArea(z3_1,z3_2,z3_3))

#kolejność dla czworokąta przyjęta dla osiągnięcia prostopadłościanu :)
print(Shapes.QuadCirc(z3_1,z3_2,z3_4,z3_3))
print(Shapes.QuadArea(z3_1,z3_2,z3_4,z3_3))

#print(Shapes.TriCirc(z3_1,2,7))

#zad4
print('------------zad4-------------')

class DecorCount:
  funcs={}
  def __init__(self,pf):
    self._pf=pf
    self._count=0
    DecorCount.funcs[pf]=self

  def __call__(self,p):
    self._count+=1
    return self._pf(p)

  @staticmethod
  def all_counts():
    return dict((fun.__name__,DecorCount.funcs[fun]._count) for fun in DecorCount.funcs)

@DecorCount
def fsum(p):
  return sum(p)

@DecorCount
def frange(p):
  return range(p)

@DecorCount
def foo(p):
  return 0

for _ in range(7):
  fsum(range(10))

for _ in range(9):
  frange(2)

print(DecorCount.all_counts())

for _ in frange(9):
  foo(1)

print(DecorCount.all_counts())



