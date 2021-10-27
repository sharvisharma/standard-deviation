import math
import csv

with open("data.csv", newline="") as f:
    reader= csv.reader(f)
    fileData= list(reader)

fileData.pop(0)
data=[]
for i in range(0,len(fileData)-1):
    value=fileData[i][1]
    data.append(value)


def mean():
    total=0

    for i in data:
        total=total+int(i)

    mean=total/len(data)
    return mean

squaredList=[]
for i in data:
    ans=int(i) - mean()
    ans=ans**2
    squaredList.append(ans)

sum=0
for i in squaredList:
    sum=sum+i

result=sum/len(squaredList)

standardDeviation=math.sqrt(result)
print(standardDeviation)


