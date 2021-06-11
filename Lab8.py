#zad1
print('------------zad1-------------')

def fun1(plik,n):
  with open(plik) as pl1:
    wiersze=pl1.readlines()
    print(wiersze[:n])
    print(wiersze[-n:])
    print(wiersze[::n])
    print([w.split()[n-1] for w in wiersze])
    print([w[n-1] for w in wiersze])

fun1("data/zad1.in",3)

#zad2
print('------------zad2-------------')
import numpy
import glob

datalist=[]
for pliki in glob.glob("data/data*.in"):
  with open(pliki) as pl2:
    wiersze=pl2.readlines()
    wiersze=[float(x) for x in wiersze]
    datalist.append(wiersze)

srednie=list(map(numpy.average,zip(*datalist)))
odchylenie=list(map(numpy.std,zip(*datalist)))

with open("data.out","w") as pl2out:
  for x in range(len(datalist[0])):
    pl2out.write(f'{x} {srednie[x]} {odchylenie[x]}\n')

#zad3
print('------------zad3-------------')

def fun3():
  pl3=open("zad3.txt","w")
  pl3.writelines('''Matplotlib jest biblioteką do tworzenia wykresów (https://matplotlib.org/). Wykorzystamy ją do wygenerowania prostego wykresu. Poniżej minimum konieczne, aby ten cel osiągnąć:

  import matplotlib.pyplot as plt
  #wyrysowanie krzywej y(x), 'o' oznacza styl punktu
plt.plot(x, y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnościami
plt.errorbar(x, y, marker='*', yerr=dy)
#opis osi
plt.xlabel('x')
#zapis do pliku, format określony przez rozszerzenie w nazwie
plt.savefig('res.pdf')

A to może się przydać do łatwego wczytywania plików (ale dzisiaj można z tego skorzystać tylko w skrypcie generującym wykresy)

import numpy
x,y=numpy.loadtxt(nazwa, unpack=True)''') 
  pl3.close()

fun3()

#zad4
print('------------zad4-------------')

nameslist=[]
ranklist=[]
for pliki in glob.glob("rank/*.txt"):
  with open(pliki) as pl4:
    wiersze=pl4.readlines()
    for w in wiersze:
      if w.split()[0] not in nameslist:
        nameslist.append(w.split()[0])

for x in nameslist:
  ranklist.append([x,['-']*21])

yearcount=0
for pliki in glob.glob("rank/*.txt"):
  with open(pliki) as pl4:
    wiersze=pl4.readlines()
    for w in wiersze:
      for osoba in ranklist:
        if w.split()[0] == osoba[0]:
          osoba[1][yearcount]=float(w.split()[1]) 
  yearcount+=1

with open("rank.out","w") as pl4out:
  pl4out.write('Nazwisko\t 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2015 2017 2018 2019 2010\n')
  for i in ranklist:
    pl4out.write(f'{i[0]}\t')
    for j in range(21):
      pl4out.write(f'{i[1][j]} ')
    pl4out.write('\n')
