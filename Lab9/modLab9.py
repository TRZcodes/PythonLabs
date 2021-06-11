from math import factorial 
def PascTri(n):
  for i in range(n):
    for j in range(n-i+1):
      print(end="  ")
    for j in range(i+1):
      print(factorial(i)//(factorial(j)*factorial(i-j)),end="   ")
    print("\n")


def Euler(n,k):
  if n<k or k==0:
    return 1
  if k==n:
    return 0
  return (k+1)*Euler(n-1,k)+(n-k)*Euler(n-1,k-1)

def EulerTri(n):
  print('n/k',end='\t')
  for i in range(n):
    print(i,end='\t')
  print('\n')
  for i in range(n):
    print(i,end='\t')
    for j in range(i+1):
      print(Euler(i,j),end='\t')
    print('\n')
  
def MakeCaesar(n):
  Translate=dict((i,97+(i+n-97)%26) for i in range(97,123))
  upperTranslate=dict((i,65+(i+n-65)%26) for i in range(65,91))
  Translate.update(upperTranslate)
  
  with open('tekstPL.txt') as pl1:
   with open('CezarOut.txt','w') as pl2:
    wiersze=pl1.readlines()
    for line in wiersze:
      pl2.write(line.translate(Translate))


def ReadCaesar(n):
  Translate=dict((i,97+(i-97-n)%26) for i in range(97,123))
  upperTranslate=dict((i,65+(i-n-65)%26) for i in range(65,91))
  Translate.update(upperTranslate)
  
  with open('CezarOut.txt') as pl1:
   with open('CezarOdczyt.txt','w') as pl2:
    wiersze=pl1.readlines()
    for line in wiersze:
      pl2.write(line.translate(Translate))


def FreqTrans(plik):
  with open('czestosci.txt') as pl1:
    freqPL={}
    wiersze=pl1.readlines()
    for line in wiersze:
      freqPL.setdefault(line[0],float(line[2:]))
    
  newFreq=dict.fromkeys(freqPL.keys(),0.)
  newFreq.setdefault('x',0.0)
  newFreq.setdefault('q',0.0)
  newFreq.setdefault('v',0.0)
  with open(plik) as pl2:
    text=pl2.read()
    textLen=0
    for i in text:
      if i.isalpha():
        textLen+=1
        newFreq[i.lower()]+=1.0
    for j in newFreq.keys():
      newFreq[j]=(newFreq[j]/textLen)*100
  print(newFreq)      

      
  




if __name__=='__main__':
  print('Hi, this is a module. Please dont use it as a main file. With kind regards, author')
  pass
