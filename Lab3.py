#!/usr/bin/env python3
import sys

#zad1
if len(sys.argv)<2:
  print("Podaj przynajmniej jeden argument wywołania")
else:
  argstr=''.join(sys.argv[1:])

print(argstr)

#zad2
lowercase=[i for i in argstr if i.islower()]
uppercase=[i for i in argstr if i.isupper()]
numbers=[int(i) for i in argstr if i.isnumeric()]
others=[i for i in argstr if not i.isalpha()]

print(lowercase)
print(uppercase)
print(numbers)
print(others)

#zad3
lowerindiv=[]
for i in lowercase:
  if i not in lowerindiv:
    lowerindiv.append(i)

print(lowerindiv)

lowercount=[(i,lowercase.count(i)) for i in lowerindiv]
print(lowercount)

#zad4
lowercount.sort(key=lambda x : x[1],reverse=True)
print(lowercount)

#zad5
smglsk='AaEeIiOoUuYy'
a=sum(argstr.count(i) for i in smglsk)
b=len(argstr)-len(others)-a
axb=[(i,a*i+b) for i in numbers]
print(axb)

#zad6
avgx=sum(numbers)/len(numbers)
avgy=sum([j for i,j in axb])/len(axb)
D=sum([((i-avgx)**2) for i in numbers])
a=sum([j*(i-avgx) for i,j in axb])/D
b=avgy-a*avgx
print(a,b)