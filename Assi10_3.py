from functools import reduce

def CheckNum(No):
    return (No>=70 and No<=90)

def Increse(No):
    return No+10

def Product(No1,No2):
    return No1*No2

print("Enter the size of list")
size = int(input())
data = list()
print("Enter the values:")
for i in range(size):
    no = int(input())
    data.append(no)

FData = list(filter(CheckNum,data))
print("filter data ",FData)

MData = list(map(Increse,FData))
print("map Data :",MData)

RData = reduce(Product,MData)
print("reduce data is",RData)
