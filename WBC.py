# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.



import numpy as np
import random
mu, sigma = 0, 0.1 # mean and standard deviation
sample=1000
sample=sample


obArray=["US","UK","AU","NZ"]
loArray=[]
for i in range(len(obArray)):
    tem=[]
    list1 = [1, 2, 3, 4, 5, 6]
    l=random.choice(list1)
    list2 = [1, 2, 3, 4, 5, 6,7,8,9,10]
    center=random.choice(list2)


    for i in range(l):
        lo=[0,0]
        s1 = np.random.normal(center, sigma, 10)

        lo=[s1[0],s1[1]]
        tem.append(lo.copy())
    
    print(tem)
    loArray.append(tem.copy())

print(loArray)

# no timezone
sampleSize=sample
data=[None] * sampleSize
tem=[0,0,0,0]
sArray=[]
for i in range(4):
    s2 = np.random.normal(mu, sigma, sample)
    sArray.append(s2)
s1 = np.random.normal(mu, sigma, sample)

set1 = set()
from datetime import datetime
# Getting the current date and time
dt = datetime.now()

# getting the timestamp

obsLen=len(obArray)
for i in range(sampleSize):
    tem=["",0.0,0.0,""]
    ts = datetime.timestamp(dt)+600*i
    dt = datetime.fromtimestamp(ts)
    c=random.random()*40
    obIndex=round(random.random()*(obsLen-1))

    loLen=len(loArray[obIndex])
    lo=loArray[obIndex][round(random.random()*(loLen-1))]
    s2 = np.random.normal(mu, sigma, sample)
    tem=[dt,c,lo,obArray[obIndex]]
    data[i]=tem.copy();
    
print(data)
