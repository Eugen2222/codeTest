# By Samuel 20220725


def getMonthDays(m,isLeap):
    days=0
    m-=1
    if(m<1):
        return 0
   

   
    mArray=[31,30,31,30,31,30,31,31,30,31,30,31]
   
    for i in range(m):
        days+=mArray[i]
   
    if m>1:
        if isLeap>0:
            days-=1
        else:
            days-=2

   
    return days

def getDays(date_string):

   
    month=0
    day=0
    year=0
   
    tem=date_string.split("/")

    day=int(tem[0])
    month=int(tem[1])
    year=int(tem[2])

    isLeap=0
    if year%4==0:
        if year%100==0:
            if year%400==0:
                isLeap=1
        else:
            isLeap=1
    year-=1    
    sum=year*365+year//400-year//100+year//4


    sum+=getMonthDays(month,isLeap)+day

    # print(getMonthDays(month,isLeap))

    return sum

def getElapsedDays(a,b):
    aDays=getDays(a)
    bDays=getDays(b)
    diff = abs(aDays-bDays)
    if diff>0:
        diff-=1
    return diff

print("**************TEST CASE************")
assert getElapsedDays("02/06/1983","22/06/1983")== 19
print("************")
assert getElapsedDays("04/07/1984","25/12/1984")== 173
print("************")
assert getElapsedDays("03/01/1989","03/08/1983")== 1979


from datetime import datetime
import random
import time
from datetime import date    

# random generate date
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def random_date():
    start="01/01/1901"
    end="31/12/2999"
    prop=random.random()
    return str_time_prop(start, end, '%d/%m/%Y', prop)

# use date lib to calculate day diff 
def getLibDays(a):
    aTem=a.split("/")
    aY=int(aTem[2])
    aM=int(aTem[1])
    aD=int(aTem[0])
    date0 = date(aY, aM, aD)
    return date0
   
def getLibDiff(a,b):

    delta = getLibDays(a) - getLibDays(b)
    days=abs(delta.days)
    if days>0:
        days-=1
    return int(days)


#compare the results from self diff function with lib diff function
error=0
for i in range(1000):
    aTest=random_date()
    bTest=random_date()
   
    libDelta=getLibDiff(aTest,bTest)
    selfDelta=getElapsedDays(aTest,bTest)
    # print(getLibDiff("01/01/4","01/01/5"))
    # print(getElapsedDays("01/01/2020","01/01/2021"))
    # print(getElapsedDays("01/01/2020","01/03/2020"))
    # print("aaaa")
    # print("self:"+str(selfDelta))
    # print("lib:"+str(libDelta))
    if libDelta!=selfDelta:
        error+=1

assert error==0





#validate input
def checkInput(input):
    print(input)
    try:
        for i in range( len(input)) :
            c=input[i]
            if c=='/' or c<='9' and c>='0':
                if c=='/':
                    if i!=2 and i!=5:
                     
                        return False
                elif (c<='9' and c>='0') and (i==2 or i==5 ):
                       
                        return False
            else:
 
                return False
        month=0
        day=0
        year=0
       
        tem=input.split("/")

        day=int(tem[0])
        month=int(tem[1])
        year=int(tem[2])
        isLeap=0
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    isLeap=1
            else:
                isLeap=1
               
        if month>12:
            return False
        if day>31:
            return False
        mArray=[31,30,31,30,31,30,31,31,30,31,30,31]   
        if month==2:
                if isLeap<1 and day>28:
                    return False
                elif day>29:
                    return False
        elif day>mArray[month-1]:
                return False
        return True
    except:

        return False
#console input function
def play():
    again=True
    firstDate=""
    secondDate=""
    while(again):
        firstDate = input("Enter the first date:")
        if checkInput(firstDate) :
            again=False
        else:
            print("Error format.")
    again=True
    while(again):
        secondDate = input("Enter the second date:")
        if checkInput(secondDate) :
            again=False
        else:
            print("Error format.")
    print("The elapsed days is:")
    print(getElapsedDays(firstDate,secondDate))
#play five times
i=5
while(i>0):
    play()
    i-=1