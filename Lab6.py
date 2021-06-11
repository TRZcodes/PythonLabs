#zad1
print('------------zad1-------------')
import time
import sys
powt = 1000
N = 10000


def forStatement():
    out = []
    for i in range(N):
        out.append(i)
    return out


def listComprehension():
    return [i for i in range(N)]


def mapFunction():
    return map(lambda x: x, range(N))


def generatorExpression():
    return (i for i in range(N))


def tester(fun):
    t = time.time_ns()
    for _ in range(powt):
      fun()
    t = time.time_ns() - t
    return t



print(sys.version)
test = (forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

'''
TEST1
3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 2378160813
listComprehension    => 1097277561
mapFunction          => 991011
generatorExpression  => 1086636


TEST2 kazde i zamienione na i**2
3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 8539022359
listComprehension    => 7562775229
mapFunction          => 1516385
generatorExpression  => 2714834

TEST 3 funkcja tester zamieniona na taka forme:

def tester(fun):
    t = time.time_ns()
    for _ in range(powt):
      suma=0
      for i in fun():
        suma+=i
    t = time.time_ns() - t
    return t

3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 3266408349
listComprehension    => 2387653615
mapFunction          => 4412988696
generatorExpression  => 4887976396

TEST 4 funkcja tester zamieniona na taka forme:

def tester(fun):
    t = time.time_ns()
    for _ in range(powt):
      sum(fun())
    t = time.time_ns() - t
    return t

3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 2210805211
listComprehension    => 1079313932
mapFunction          => 2222172785
generatorExpression  => 1116795364

TEST 5 funkcja mapFunction zamieniona na taka forme:
def mapFunction():
    return list(map(lambda x: x, range(N)))

funkcja generatorExpression zamieniona na taka forme:
def generatorExpression():
    return list((i for i in range(N)))

3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 3264076431
listComprehension    => 1569923486
mapFunction          => 3224209627
generatorExpression  => 2218762070
'''

#zad2
print('------------zad2-------------')
import random
n = 1000000

points = [random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2 for _ in range(n)]
pi = len(list(filter(lambda x: x <= 1, points))) * 4 / n
print("Przyblizenie liczby pi:", pi)

#zad3
print('------------zad3-------------')

matrix1=[[1,3,7],[2,5,8],[4,1,3]]
matrix2=[[4,5,8],[1,0,3],[6,1,9]]
matrix3=[[4,5,8],[1,0,3],[6,1,9]]

print(list(map(max,matrix1))) #maksimum wiersza macierzy

print(list(map(max,zip(*matrix1)))) #maksimum kolumny macierzy

print([list(map(sum,zip(*i))) for i in zip(matrix1,matrix2,matrix3)]) #suma macierzy

#zad5
from functools import reduce
from math import sqrt
print('------------zad5-------------')
def fun5(list1, list2):
  elems=len(list1)
  xsrednie=reduce(lambda x,y: x+y, list1)/elems
  ysrednie=reduce(lambda x,y: x+y, list2)/elems
  D=reduce(lambda x,y: x+y,list(map(lambda x: (x-xsrednie)**2,list1)))
  a=reduce(lambda x,y: x+y,list(map(lambda x,y: y*(x-xsrednie),list1,list2)))/D
  b=ysrednie-a*xsrednie
  yblad=sqrt(reduce(lambda x,y: x+y,list(map(lambda x,y:(y-a*x-b)**2,list1,list2)))/(elems-2))
  ablad=yblad/sqrt(D)
  bblad=yblad*sqrt((1/n)+((xsrednie**2)/D))
  
  print("Dofitowana wartosc a:",a)
  print("Dofitowana wartosc b:",b)
  print("Niepewnosc wartosci a:",ablad)
  print("Niepewnosc wartosci b:",bblad)

fun5([1,2,3],[4,5,6])
