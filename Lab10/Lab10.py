#zad1
print('------------zad1-------------')

from datetime import date

def dec_val(rok):
  if rok<1900:
    return 80
  elif rok<2000:
    return 0
  elif rok<2100:
    return 20
  elif rok<2200:
    return 40
  elif rok<2300:
    return 60


def CheckPesel(pesel, data, sex):
  rok=pesel[:2]
  mon=pesel[2:4]
  miesiac=int(mon)%20
  decade_num=int(mon)-miesiac
  dzien=pesel[4:6]
  sex_check=1 if sex=='m' else 0


  ctrl=[1,3,7,9,1,3,7,9,1,3]
  sumctrl=0
  for i in range(10):
    sumctrl+=int(pesel[i])*ctrl[i]
  sumctrl=sumctrl%10
  sumctrl=(10-sumctrl)%10


  if int(rok)==data.year%100 and miesiac==data.month and int(dzien)==data.day and decade_num==dec_val(data.year) and (int(pesel[9]))%2==sex_check and sumctrl==int(pesel[10]):
    return True
  return False


print(CheckPesel("02070803628",date(1902,7,8),'f'))
print(CheckPesel("02270803624",date(2002,7,8),'f'))
print(CheckPesel("02270812350",date(2002,7,8),'m'))

#zad2
print('------------zad2-------------')


def AvgAge(file,mode):
  days=[31,28,31,30,31,30,31,31,30,31,30,31]
  ageCount=0.0
  dateCount=0.0
  with open(file) as f:
    daty=f.readlines()
    for i in daty:
      dateTab=i.split()
      try:  
        if len(dateTab)!=3 and mode=='r':
          raise IndexError
        elif len(dateTab)!=3:
          continue
        dzien=int(dateTab[0])
        miesiac=int(dateTab[1])
        rok=int(dateTab[2])
        if (rok%4 and not rok%100) or rok%400:
          if miesiac==2 and dzien<=29:
            dateCount+=1
            ageCount+=(2021-rok)
          elif dzien<=days[miesiac-1]:
            dateCount+=1
            ageCount+=(2021-rok)
          elif mode=='r':
              raise
        else:
          if dzien<=days[miesiac-1]:
            dateCount+=1
            ageCount+=(2021-rok)
          elif mode=='r':
              raise
      except IndexError:
        print("Zly format daty")
        return 0
      except:
        print("Niepoprawna data")
        return 0
  return ageCount/dateCount

print(AvgAge("daty.in",'l'))    
print(AvgAge("daty.in",'r')) 

#zad3
print('------------zad3-------------')

def PitCheck(nums):
  check=True
  try:
    if(len(nums)<3):
      raise IndexError
    for i in range(len(nums)-2):
      a=nums[i]**2
      b=nums[i+1]**2
      c=nums[i+2]**2
      if a+b==c:
        check=False
        parz=0
        for j in range(3):
          if nums[i+j]%2==0:
            parz+=1
        print("Trójka pitagorejska: ",nums[i],nums[i+1],nums[i+2], "Parzyste: ",parz," Nieparzyste: ", 3-parz)
    for i in range(len(nums)-3):
      a=nums[i]**2
      b=nums[i+1]**2
      c=nums[i+2]**2
      d=nums[i+3]**2
      if a+b+c==d:
        check=False
        parz=0
        for j in range(4):
          if nums[i+j]%2==0:
            parz+=1
        print("Czwórka pitagorejska: ",nums[i],nums[i+1],nums[i+2],nums[i+3], "Parzyste: ",parz," Nieparzyste: ", 4-parz)
    if check:
      raise
  except IndexError:
    print("Lista jest zbyt krótka")
  except:
    print("Nie wystąpiła żadna trójka/czwórka pitagorejska")

l1=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
l2=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)
l3=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
l4=(1,2,3,4,5,6,7,8,9)  
l5=(1,2)
l6=(1,2,2,7)

PitCheck(l1)
#PitCheck(l2)
#PitCheck(l3)
#PitCheck(l4)
#PitCheck(l5)
#PitCheck(l6)
