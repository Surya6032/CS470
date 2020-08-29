import random
from math import log,floor
number=int(input("How many random numbers to be generated:"))
i = log(number) / log(10)
if i - floor(i) < 0.000001:
  print("yes")

threeEnd=0
sevenEnd=0
threeF=0
sevenF=0
for i in range(number):
    rand = random.randint(0, 999)
    if rand%10==3:
      threeEnd=threeEnd+1
    elif rand%10==7:
      sevenEnd=sevenEnd+1
    if int(str(rand)[:1])==3:
      threeF=threeF+1
    if int(str(rand)[:1])==7:
      sevenF=sevenF+1
    print(rand)
print("Three End:",threeEnd)
print("Seven End:",sevenEnd)
print("Three First:",threeF)
print("Seven First:",sevenF)
